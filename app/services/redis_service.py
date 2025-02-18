import os

import redis


class RedisService:
    DEFAULTS = {
        type(float): 0,
        type(int): 0,
        type(str): "",
        type(bool): False,
    }

    def __init__(self):
        self.connection = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            decode_responses=True
        )

    def get(self, key: str, datatype: type):
        val = self.connection.get(key)
        return datatype(val if val is not None else self.DEFAULTS[datatype])

    def set(self, key: str, val):
        self.connection.set(key, str(val))
