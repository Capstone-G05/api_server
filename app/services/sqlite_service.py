import os
import sqlite3


from utils.parameters import Parameter as P

class SQLiteService:
    DEFAULTS = [
        (P.PIVOT_ANGLE_MAX.name, "90"),
        (P.PIVOT_ANGLE_MIN.name, "0"),
        (P.PIVOT_SPEED_REFERENCE.name, "30"),
        (P.FOLD_ANGLE_MAX.name, "90"),
        (P.FOLD_ANGLE_MIN.name, "0"),
        (P.FOLD_SPEED_REFERENCE.name, "30"),
        (P.TILT_ANGLE_MAX.name, "90"),
        (P.TILT_ANGLE_MIN.name, "0"),
        (P.TILT_SPEED_REFERENCE.name, "30"),
        (P.ROTATE_ANGLE_MAX.name, "180"),
        (P.ROTATE_ANGLE_MIN.name, "90"),
        (P.ROTATE_SPEED_REFERENCE.name, "30"),
        (P.GATE_ANGLE_MIN.name, "90"),
        (P.GATE_ANGLE_MIN.name, "0"),
        (P.GATE_SPEED_REFERENCE.name, "30"),
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
