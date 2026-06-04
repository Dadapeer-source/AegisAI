import psutil
from datetime import datetime


class SystemCollector:

    def collect(self):
        try:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            net = psutil.net_io_counters()
            network_sent = net.bytes_sent
            network_received = net.bytes_recv

            process_count = len(psutil.pids())

            data = {
                "timestamp": datetime.now(),
                "cpu_usage": cpu,
                "memory_usage": memory,
                "disk_usage": disk,
                "network_sent": network_sent,
                "network_received": network_received,
                "process_count": process_count
            }

            return data

        except Exception as e:
            print("❌ System collection error:", e)
            return None