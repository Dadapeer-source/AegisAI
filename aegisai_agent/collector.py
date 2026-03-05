import psutil
from datetime import datetime

def collect_system_metrics():
    return {
        "timestamp": datetime.now(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('C:\\').percent,  # Windows fix
        "net_sent": psutil.net_io_counters().bytes_sent,
        "net_recv": psutil.net_io_counters().bytes_recv
    }


def collect_processes():
    process_list = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
        try:
            process_list.append({
                "timestamp": datetime.now(),
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu": proc.info['cpu_percent'],
                "memory": proc.info['memory_percent'],
                "status": proc.info['status']
            })
        except:
            continue

    # 🔥 THIS IS WHERE YOU ADD YOUR LINE
    process_list = sorted(process_list, key=lambda x: x['cpu'], reverse=True)[:10]

    return process_list