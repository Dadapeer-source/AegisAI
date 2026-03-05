import mysql.connector
from config import DB_CONFIG


class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            print("✅ Connected to MySQL successfully")
        except Exception as e:
            print("❌ Database connection failed:", e)

    # 🔹 Insert system metrics
    def insert_system_metrics(self, data):
        query = """
        INSERT INTO system_metrics 
        (timestamp, cpu_usage, memory_usage, disk_usage, network_sent, network_recv)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data["timestamp"],
            data["cpu"],
            data["memory"],
            data["disk"],
            data["net_sent"],
            data["net_recv"]
        )

        try:
            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print("❌ System insert failed:", e)

    # 🔥 Batch insert for processes (FAST)
    def insert_processes_batch(self, process_list):
        query = """
        INSERT INTO processes 
        (timestamp, pid, name, cpu_percent, memory_percent, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = [
            (
                p["timestamp"],
                p["pid"],
                p["name"],
                p["cpu"],
                p["memory"],
                p["status"]
            )
            for p in process_list
        ]

        try:
            self.cursor.executemany(query, values)
            self.conn.commit()
        except Exception as e:
            print("❌ Batch insert failed:", e)

    # 🚨 Insert alerts (NEW)
    def insert_alert(self, alert_type, message):
        query = """
        INSERT INTO alerts (timestamp, alert_type, message)
        VALUES (NOW(), %s, %s)
        """

        try:
            self.cursor.execute(query, (alert_type, message))
            self.conn.commit()
        except Exception as e:
            print("❌ Alert insert failed:", e)