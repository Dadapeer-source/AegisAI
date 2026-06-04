import time

from collector.system_collector import SystemCollector
from collector.process_collector import ProcessCollector
from database.insert_queries import InsertQueries


def run_monitoring():

    system_collector = SystemCollector()
    process_collector = ProcessCollector()
    inserter = InsertQueries()

    print("🚀 AegisAI Monitoring Started...")

    while True:
        try:
            # Collect data
            system_data = system_collector.collect()
            process_data = process_collector.collect()

            # Insert into database
            if system_data:
                inserter.insert_system_metrics(system_data)

            if process_data:
                inserter.insert_process_metrics(process_data)

            print("✅ Data cycle completed")

            # Wait 5 seconds
            time.sleep(5)

        except Exception as e:
            print("❌ Error in monitoring loop:", e)
            time.sleep(5)


if __name__ == "__main__":
    run_monitoring()