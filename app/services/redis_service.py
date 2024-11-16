# app/redis_service.py
import redis
rd_connection = None

default = 00 # Default if key does not exist

# move password to env file later?
def connect_redis():
    global rd_connection 
    rd_connection = redis.StrictRedis(host="172.23.24.2",  port=6379, password="graincart", decode_responses=True )

def disconnect_redis():
    global rd_connection 
    rd_connection = None 

def load_data_to_redis():
    
    #to avoid circular dependency
    from services.db_service import db_connection

    global rd_connection

    cursor = db_connection.cursor()
    cursor.execute("SELECT key, value FROM redis_keys")
    rows = cursor.fetchall()

    # Load data into Redis
    for key, value in rows:
        rd_connection.set(key, value)
        print(f"Loaded {key} = {value} into Redis")

#auger
def get_auger_pivot_angle():
    value = rd_connection.get("auger_pivot_angle")
    return float(value) if value is not None else default
    
def get_auger_pivot_angle_max():
    value = rd_connection.get("auger_pivot_angle_max")
    return float(value) if value is not None else default

def get_auger_pivot_angle_min():
    value = rd_connection.get("auger_pivot_angle_min")
    return float(value) if value is not None else default

def get_auger_fold_angle():
    value = rd_connection.get("auger_fold_angle")
    return float(value) if value is not None else default
    
def get_auger_fold_angle_max():
    value = rd_connection.get("auger_fold_angle_max")
    return float(value) if value is not None else default

def get_auger_fold_angle_min():
    value = rd_connection.get("auger_fold_angle_min")
    return float(value) if value is not None else default



#spout
def get_spout_tilt_angle():
    value = rd_connection.get("spout_tilt_angle")
    return float(value) if value is not None else default
    
def get_spout_tilt_angle_max():
    value = rd_connection.get("spout_tilt_angle_max")
    return float(value) if value is not None else default

def get_spout_tilt_angle_min():
    value = rd_connection.get("spout_tilt_angle_min")
    return float(value) if value is not None else default

def get_spout_rotation_angle():
    value = rd_connection.get("spout_rotation_angle")
    return float(value) if value is not None else default
    
def get_spout_rotation_angle_max():
    value = rd_connection.get("spout_rotation_angle_max")
    return float(value) if value is not None else default

def get_spout_rotation_angle_min():
    value = rd_connection.get("spout_rotation_angle_min")
    return float(value) if value is not None else default

#gate
def get_gate_angle():
    value = rd_connection.get("gate_angle")
    return float(value) if value is not None else default
    
def get_gate_angle_max():
    value = rd_connection.get("gate_angle_max")
    return float(value) if value is not None else default

def get_gate_angle_min():
    value = rd_connection.get("gate_angle_min")
    return float(value) if value is not None else default
    
    
#reference speeds
def get_auger_pivot_speed():
    value = rd_connection.get("auger_pivot_speed_ref")
    return float(value) if value is not None else default

def get_auger_fold_speed():
    value = rd_connection.get("auger_fold_speed_ref")
    return float(value) if value is not None else default

def get_spout_tilt_speed():
    value = rd_connection.get("spout_tilt_speed_ref")
    return float(value) if value is not None else default

def get_spout_rotation_speed():
    value = rd_connection.get("spout_rotation_speed_ref")
    return float(value) if value is not None else default

def get_gate_speed():
    value = rd_connection.get("gate_speed_ref")
    return float(value) if value is not None else default

