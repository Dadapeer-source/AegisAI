from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psutil
import os
import time
import win32gui
import win32process

from automation.actions import Actions
from logic.failure_predictor import FailurePredictor
from logic.decision_engine import DecisionEngine

app = FastAPI(title="AegisAI Brain API")

actions = Actions()
predictor = FailurePredictor()
decision_engine = DecisionEngine()

# 🔥 Mitigation threshold (when killing starts)
SAFE_CPU_LEVEL = 95

SAFE_PROCESS_NAMES = [
    "system",
    "system idle process",
    "services.exe",
    "wininit.exe",
    "lsass.exe",
    "csrss.exe",
    "smss.exe",
    "explorer.exe",
    "python.exe",
    "uvicorn.exe"
]

CURRENT_PID = os.getpid()
LAST_ACTION_TIME = 0
ACTION_COOLDOWN = 10

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def get_status():

    global LAST_ACTION_TIME

    try:
        cpu = psutil.cpu_percent(interval=0.5)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("C:\\").percent
        process_count = len(psutil.pids())

        risk = predictor.calculate_risk(cpu, memory, disk, process_count)
        decision = decision_engine.decide(False, risk)

        current_time = time.time()

        if cpu >= SAFE_CPU_LEVEL:
            if current_time - LAST_ACTION_TIME > ACTION_COOLDOWN:
                if decision == "KILL_PROCESS":
                    kill_memory_priority_process()
                    LAST_ACTION_TIME = current_time

        return {
            "cpu": round(cpu, 1),
            "memory": round(memory, 1),
            "disk": round(disk, 1),
            "process_count": process_count,
            "risk": risk,
            "decision": decision
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 🔥 SAFE BACKGROUND PRIORITY KILL FUNCTION

def get_foreground_pid():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        return pid
    except:
        return None


def kill_memory_priority_process():

    print("🔍 Searching for heavy BACKGROUND process...")

    active_pid = get_foreground_pid()
    candidates = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']

            if not name:
                continue

            name_lower = name.lower()

            # ❌ Protect system
            if pid in (0, 4):
                continue

            # ❌ Protect backend
            if pid == CURRENT_PID:
                continue

            # ❌ Protect active foreground app
            if pid == active_pid:
                continue

            # ❌ Protect safe list
            if name_lower in SAFE_PROCESS_NAMES:
                continue

            cpu = proc.cpu_percent(interval=0.2)
            mem = proc.memory_percent()

            # 🔥 Memory weighted priority
            score = (mem * 3) + cpu

            if mem > 1 or cpu > 5:
                candidates.append((score, mem, cpu, proc))

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not candidates:
        print("No suitable background process found.")
        return

    candidates.sort(reverse=True, key=lambda x: x[0])

    highest_score, mem, cpu, target = candidates[0]

    print(f"🔥 Killing {target.pid} ({target.name()}) | MEM: {mem:.2f}% | CPU: {cpu:.2f}%")

    try:
        target.kill()
        print("✅ Background process killed successfully")
    except Exception as e:
        print("⚠ Kill failed:", e)