import os

import redis

rd_connection = None

DEFAULT = 00  # default if key does not exist


def connect_redis():
    global rd_connection
    rd_connection = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        decode_responses=True
    )


def disconnect_redis():
    global rd_connection
    rd_connection = None


def load_data_to_redis():
    # to avoid circular dependency
    from services.db_service import db_connection

    global rd_connection

    cursor = db_connection.cursor()
    cursor.execute("SELECT key, value FROM redis_keys")
    rows = cursor.fetchall()

    # Load data into Redis
    for key, value in rows:
        rd_connection.set(key, value)
        print(f"Loaded {key} = {value} into Redis")


# set frontend parameters in redis
def set_in_redis(key, value):
    rd_connection.set(key, value)


# auger
def get_auger_pivot_angle():
    value = rd_connection.get("auger_bottom_pivot_angle")
    return float(value) if value is not None else DEFAULT


def get_auger_pivot_angle_max():
    value = rd_connection.get("auger_bottom_pivot_angle_max")
    return float(value) if value is not None else DEFAULT


def get_auger_pivot_angle_min():
    value = rd_connection.get("auger_bottom_pivot_angle_min")
    return float(value) if value is not None else DEFAULT


def get_auger_top_angle():
    value = rd_connection.get("auger_top_angle")
    return float(value) if value is not None else DEFAULT


def get_auger_top_angle_max():
    value = rd_connection.get("auger_top_angle_max")
    return float(value) if value is not None else DEFAULT


def get_auger_top_angle_min():
    value = rd_connection.get("auger_top_angle_min")
    return float(value) if value is not None else DEFAULT


# spout
def get_spout_tilt_angle():
    value = rd_connection.get("spout_tilt_angle")
    return float(value) if value is not None else DEFAULT


def get_spout_tilt_angle_max():
    value = rd_connection.get("spout_tilt_angle_max")
    return float(value) if value is not None else DEFAULT


def get_spout_tilt_angle_min():
    value = rd_connection.get("spout_tilt_angle_min")
    return float(value) if value is not None else DEFAULT


# head
def get_head_rotation_angle():
    value = rd_connection.get("head_rotation_angle")
    return float(value) if value is not None else DEFAULT


def get_head_rotation_angle_max():
    value = rd_connection.get("head_rotation_angle_max")
    return float(value) if value is not None else DEFAULT


def get_head_rotation_angle_min():
    value = rd_connection.get("head_rotation_angle_min")
    return float(value) if value is not None else DEFAULT


# gate
def get_gate_angle():
    value = rd_connection.get("gate_angle")
    return float(value) if value is not None else DEFAULT


def get_gate_angle_max():
    value = rd_connection.get("gate_angle_max")
    return float(value) if value is not None else DEFAULT


def get_gate_angle_min():
    value = rd_connection.get("gate_angle_min")
    return float(value) if value is not None else DEFAULT


# reference speeds
def get_auger_bottom_pivot_speed():
    value = rd_connection.get("auger_bottom_pivot_speed_ref")
    return float(value) if value is not None else DEFAULT


def get_auger_top_speed():
    value = rd_connection.get("auger_top_speed_ref")
    return float(value) if value is not None else DEFAULT


def get_spout_tilt_speed():
    value = rd_connection.get("spout_tilt_speed_ref")
    return float(value) if value is not None else DEFAULT


def get_head_rotation_speed():
    value = rd_connection.get("head_rotation_speed_ref")
    return float(value) if value is not None else DEFAULT


def get_gate_speed():
    value = rd_connection.get("gate_speed_ref")
    return float(value) if value is not None else DEFAULT


# power
def get_simulation_power():
    value = rd_connection.get("simulation_power")
    if value == 'true' or value == 'True':
        return True
    else:
        return False


# pwm
def get_auger_pivot_up():
    value = rd_connection.get("auger_bottom_pivot_up_pwm")
    return float(value) if value is not None else DEFAULT


def get_auger_pivot_down():
    value = rd_connection.get("auger_bottom_pivot_down_pwm")
    return float(value) if value is not None else DEFAULT


def get_auger_fold():
    value = rd_connection.get("auger_top_fold_pwm")
    return float(value) if value is not None else DEFAULT


def get_auger_unfold():
    value = rd_connection.get("auger_top_unfold_pwm")
    return float(value) if value is not None else DEFAULT


def get_spout_tilt_up():
    value = rd_connection.get("spout_tilt_up_pwm")
    return float(value) if value is not None else DEFAULT


def get_spout_tilt_down():
    value = rd_connection.get("spout_tilt_down_pwm")
    return float(value) if value is not None else DEFAULT


def get_head_rotation_cw():
    value = rd_connection.get("head_rotation_cw_pwm")
    return float(value) if value is not None else DEFAULT


def get_head_rotation_ccw():
    value = rd_connection.get("head_rotation_ccw_pwm")
    return float(value) if value is not None else DEFAULT


def get_gate_open():
    value = rd_connection.get("gate_open_pwm")
    return float(value) if value is not None else DEFAULT


def get_gate_close():
    value = rd_connection.get("gate_close_pwm")
    return float(value) if value is not None else DEFAULT
