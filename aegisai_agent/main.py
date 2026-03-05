import time
import threading
from db import Database
from collector import collect_system_metrics, collect_processes
from config import INTERVAL
from logger import log_info, log_error
from alerts import check_system_alerts, check_process_alerts


def system_worker():
    db = Database()

    while True:
        try:
            # 🔹 Collect system data
            data = collect_system_metrics()
            db.insert_system_metrics(data)

            # 🔥 Check alerts
            check_system_alerts(data, db, log_info, log_error)

            log_info("System metrics inserted")

        except Exception as e:
            log_error(f"System thread error: {e}")

        time.sleep(INTERVAL)


def process_worker():
    db = Database()

    while True:
        try:
            # 🔹 Collect process data
            processes = collect_processes()
            db.insert_processes_batch(processes)

            # 🔥 Check alerts
            check_process_alerts(processes, db, log_info, log_error)

            log_info("Process data inserted")

        except Exception as e:
            log_error(f"Process thread error: {e}")

        time.sleep(INTERVAL)


def run():
    t1 = threading.Thread(target=system_worker)
    t2 = threading.Thread(target=process_worker)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    run()