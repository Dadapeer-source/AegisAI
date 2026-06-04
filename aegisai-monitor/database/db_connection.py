import mysql.connector
from mysql.connector import Error
from config.db_config import DB_CONFIG


class DBConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)

            if self.connection.is_connected():
                print("✅ Database connected")

        except Error as e:
            print("❌ Connection error:", e)
            self.connection = None

    def get_connection(self):
        try:
            if self.connection is None or not self.connection.is_connected():
                print("🔄 Reconnecting to database...")
                self.connect()
        except Error as e:
            print("❌ Error checking connection:", e)
            self.connect()

        return self.connection

    def get_cursor(self):
        connection = self.get_connection()

        if connection is not None:
            return connection.cursor()
        else:
            print("❌ Cannot get cursor — no connection")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 Database connection closed")