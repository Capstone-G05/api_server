import os

import redis

from utils.parameters import Parameter


class RedisService:
    DEFAULTS = {
        "float": 0,
        "int": 0,
        "str": "",
        "bool": False,
    }

    def __init__(self):
        self.connection = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            decode_responses=True
        )

    def load_data(self, database):
        cursor = database.execute("SELECT key, value FROM redis_keys")
        rows = cursor.fetchall()
        print("Loading data into Redis...")
        for key, value in rows:
            self.set(key, value)
            print(f"{key}: {value}")

    def get(self, key: str):
        return self.connection.get(key)

    def set(self, key: str, val):
        self.connection.set(key, str(val))
