from database.db_connection import DBConnection


class InsertQueries:

    def __init__(self):
        self.db = DBConnection()

    def insert_system_metrics(self, data):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO system_metrics 
                (timestamp, cpu_usage, memory_usage, disk_usage, network_sent, network_received, process_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                data["timestamp"],
                data["cpu_usage"],
                data["memory_usage"],
                data["disk_usage"],
                data["network_sent"],
                data["network_received"],
                data["process_count"]
            )

            cursor.execute(query, values)
            conn.commit()

        except Exception as e:
            print("❌ Error inserting system metrics:", e)

    def insert_process_metrics(self, processes):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO process_metrics
                (timestamp, process_id, process_name, process_cpu_usage, process_memory_usage, execution_path, parent_process)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = []

            for proc in processes:
                values.append((
                    proc["timestamp"],
                    proc["process_id"],
                    proc["process_name"],
                    proc["process_cpu_usage"],
                    proc["process_memory_usage"],
                    proc["execution_path"],
                    proc["parent_process"]
                ))

            cursor.executemany(query, values)
            conn.commit()

        except Exception as e:
            print("❌ Error inserting process metrics:", e)