import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self, db_name="speed_test.db"):
        self.db_path = Path(db_name)
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS speed_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mode TEXT,
                    download_speed REAL,
                    upload_speed REAL,
                    latency REAL,
                    execution_time REAL,
                    timestamp TEXT
                )
            """)
            conn.commit()

    def insert_result(self, result_tuple):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO speed_results
                (mode, download_speed, upload_speed, latency, execution_time, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, result_tuple)
            conn.commit()

    def fetch_all_results(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM speed_results ORDER BY id DESC")
            return cursor.fetchall()
