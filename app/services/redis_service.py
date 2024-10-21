# app/redis_service.py
import redis

connection = None

def connect_redis():
    global connection 
    connection = redis.StrictRedis(host='localhost', port=6379, db=0)

def disconnect_redis():
    global connection 
    connection = None 
