# app/redis_service.py
import redis

connection = None

default = 00 # Default if key does not exist

def connect_redis():
    global connection 
    connection = redis.StrictRedis(host="172.23.24.2",  port=6379, password="graincart", decode_responses=True )

def disconnect_redis():
    global connection 
    connection = None 

def get_auger_pivot_angle():
    value = connection.get("auger_pivot_angle")
    return float(value) if value is not None else default
    

def get_auger_pivot_angle_max():
    value = connection.get("auger_pivot_angle_max")
    return float(value) if value is not None else default

def get_auger_pivot_angle_min():
    value = connection.get("auger_pivot_angle_min")
    return float(value) if value is not None else default


def get_auger_fold_angle():
    value = connection.get("auger_fold_angle")
    return float(value) if value is not None else default
    
def get_auger_fold_angle_max():
    value = connection.get("auger_fold_angle_max")
    return float(value) if value is not None else default

def get_auger_fold_angle_min():
    value = connection.get("auger_fold_angle_min")
    return float(value) if value is not None else default


def get_spout_tilt_angle():
    value = connection.get("spout_tilt_angle")
    return float(value) if value is not None else default
    
def get_spout_tilt_angle_max():
    value = connection.get("spout_tilt_angle_max")
    return float(value) if value is not None else default

def get_spout_tilt_angle_min():
    value = connection.get("spout_tilt_angle_min")
    return float(value) if value is not None else default


def get_gate_angle():
    value = connection.get("gate_angle")
    return float(value) if value is not None else default
    
def get_gate_angle_max():
    value = connection.get("gate_angle_max")
    return float(value) if value is not None else default

def get_gate_angle_min():
    value = connection.get("gate_angle_min")
    return float(value) if value is not None else default
    
    
