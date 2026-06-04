import psutil
from datetime import datetime


class ProcessCollector:

    def collect(self, top_n=5):
        processes = []

        try:
            # Warm-up CPU readings (important)
            for proc in psutil.process_iter():
                try:
                    proc.cpu_percent(interval=None)
                except:
                    pass

            # Collect process info
            for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'exe', 'ppid']):
                try:
                    cpu = proc.cpu_percent(interval=0.1)

                    name = proc.info['name']
                    if not name:
                        continue

                    # Skip unwanted system processes
                    if name.lower() in ["system idle process", "system"]:
                        continue

                    # Filter only invalid CPU values
                    if cpu < 0 or cpu > 100:
                        continue

                    processes.append({
                        "pid": proc.info['pid'],
                        "name": name,
                        "cpu": cpu,
                        "memory": proc.info['memory_percent'],
                        "exe": proc.info['exe'] or "Unknown",
                        "ppid": proc.info['ppid']
                    })

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            # Sort by CPU usage (descending)
            processes = sorted(processes, key=lambda x: x["cpu"], reverse=True)

            # Take top processes
            top_processes = processes[:top_n]

            result = []

            for proc in top_processes:
                result.append({
                    "timestamp": datetime.now(),
                    "process_id": proc["pid"],
                    "process_name": proc["name"],
                    "process_cpu_usage": proc["cpu"],
                    "process_memory_usage": proc["memory"],
                    "execution_path": proc["exe"],
                    "parent_process": proc["ppid"]
                })

            return result

        except Exception as e:
            print("❌ Process collection error:", e)
            return []