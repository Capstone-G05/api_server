import os

import redis


class RedisService:
    def __init__(self):
        self.connection = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            decode_responses=True
        )

    def close(self):
        self.connection.close()

    def load_data(self, database):
        cursor = database.execute("SELECT key, value FROM redis_keys")
        rows = cursor.fetchall()
        for key, value in rows:
            if (existing_value := self.get(key)) is not None:
                print(f"{key}: {existing_value} (already loaded)")
            else:
                self.set(key, value)
                print(f"{key}: {value}")

        print("Redis loaded")

    def get(self, key: str):
        return self.connection.get(key)

    def set(self, key: str, val):
        self.connection.set(key, str(val))
