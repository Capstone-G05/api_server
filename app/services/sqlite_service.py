import os
import sqlite3


class SQLiteService:
    DEFAULTS = [
        ("auger_bottom_pivot_angle_max", "90"),
        ("auger_bottom_pivot_angle_min", "0"),
        ("auger_top_angle_min", "0"),
        ("auger_top_angle_max", "90"),
        ("spout_tilt_angle_min", "0"),
        ("spout_tilt_angle_max", "90"),
        ("head_rotation_angle_max", "180"),
        ("head_rotation_angle_min", "90"),
        ("gate_angle_max", "90"),
        ("gate_angle_min", "0"),
        ("auger_bottom_pivot_speed_ref", "30"),
        ("auger_top_speed_ref", "30"),
        ("spout_tilt_speed_ref", "30"),
        ("head_rotation_speed_ref", "30"),
        ("gate_speed_ref", "30")
    ]

    def __init__(self):
        self.connection = sqlite3.connect(os.getenv("DATABASE", "database.db"))
        self.initialize_database()

    def execute(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor

    def close(self):
        self.connection.close()

    def initialize_database(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS redis_keys (
                key TEXT PRIMARY KEY,
                value TEXT
            )
            """)

        cursor.execute("""DELETE FROM redis_keys""")

        cursor.executemany(
            "INSERT OR IGNORE INTO redis_keys (key, value) VALUES (?, ?)", self.DEFAULTS
        )

        self.connection.commit()

        print("Database initialized successfully with mock data!")
