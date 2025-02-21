import os
import sqlite3

from utils.parameters import Parameter as P


class SQLiteService:
    DEFAULTS = [
        (P.PIVOT_ANGLE_MAX, "90"),
        (P.PIVOT_ANGLE_MIN, "0"),
        (P.PIVOT_SPEED_REFERENCE, "30"),

        (P.FOLD_ANGLE_MAX, "90"),
        (P.FOLD_ANGLE_MIN, "0"),
        (P.FOLD_SPEED_REFERENCE, "30"),

        (P.TILT_ANGLE_MAX, "90"),
        (P.TILT_ANGLE_MIN, "0"),
        (P.TILT_SPEED_REFERENCE, "30"),

        (P.ROTATE_ANGLE_MAX, "180"),
        (P.ROTATE_ANGLE_MIN, "90"),
        (P.ROTATE_SPEED_REFERENCE, "30"),

        (P.GATE_ANGLE_MAX, "90"),
        (P.GATE_ANGLE_MIN, "0"),
        (P.GATE_SPEED_REFERENCE, "30"),

        (P.PTO_FLOW_RATE, "1"),
    ]

    def __init__(self):
        self.connection = sqlite3.connect(os.getenv("DATABASE", "database.db"))

    def execute(self, query: str, *args):
        cursor = self.connection.cursor()
        cursor.execute(query, *args)
        return cursor

    def persist(self, key: str, value):
        self.execute("""
            INSERT INTO redis_keys (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = ?;
        """, (key, value, value))

    def close(self):
        self.connection.close()

    def initialize(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS redis_keys (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        cursor = self.execute("SELECT key, value FROM redis_keys")

        existing_keys = [result[0] for result in cursor.fetchall()]

        for (param, default) in self.DEFAULTS:
            if param.name not in existing_keys:
                self.execute("INSERT INTO redis_keys (key, value) VALUES (?, ?)", (param.name, default))

        self.connection.commit()
        print("Database initialized")
