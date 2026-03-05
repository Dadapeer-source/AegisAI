import time
import psutil

# 🔹 CPU core count (for normalization)
CPU_CORES = psutil.cpu_count()

# 🔹 cooldown + tracking
last_alert_time = {}
process_counter = {}

COOLDOWN = 60  # seconds
THRESHOLD_COUNT = 3  # persistence


def should_alert(key):
    current_time = time.time()

    if key not in last_alert_time:
        last_alert_time[key] = current_time
        return True

    if current_time - last_alert_time[key] > COOLDOWN:
        last_alert_time[key] = current_time
        return True

    return False


def check_system_alerts(data, db, log_info, log_error):
    try:
        cpu = data["cpu"]
        memory = data["memory"]

        # 🔥 System-level check (already normalized)
        if cpu > 90 and should_alert("cpu"):
            msg = f"CRITICAL SYSTEM CPU usage: {cpu}%"
            db.insert_alert("CPU_CRITICAL", msg)
            log_error(msg)

        if memory > 90 and should_alert("memory"):
            msg = f"CRITICAL MEMORY usage: {memory}%"
            db.insert_alert("MEMORY_CRITICAL", msg)
            log_error(msg)

    except Exception as e:
        log_error(f"System alert error: {e}")


def check_process_alerts(processes, db, log_info, log_error):
    global process_counter

    try:
        # 🔥 Sort top 2 CPU processes only
        processes = sorted(processes, key=lambda x: x["cpu"], reverse=True)[:2]

        for p in processes:

            name = p["name"]

            # ❌ Ignore useless processes
            if name in ["System Idle Process", "System"]:
                continue

            # 🔥 Normalize CPU (multi-core fix)
            normalized_cpu = p["cpu"] / CPU_CORES

            # 🔥 Persistence logic
            if normalized_cpu > 80:
                process_counter[name] = process_counter.get(name, 0) + 1
            else:
                process_counter[name] = 0

            if process_counter[name] >= THRESHOLD_COUNT:

                key = f"proc_{name}"

                if should_alert(key):
                    msg = f"CRITICAL PROCESS: {name} ({normalized_cpu:.2f}% per core)"
                    db.insert_alert("PROCESS_CRITICAL", msg)
                    log_error(msg)

    except Exception as e:
        log_error(f"Process alert error: {e}")