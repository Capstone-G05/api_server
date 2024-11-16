# app/db_service.py
import sqlite3

db_connection = None

def connect_db(db_name: str):
    global db_connection
    db_connection = sqlite3.connect(db_name)
    initialize_database()

def disconnect_db():
    global db_connection
    if db_connection:
        db_connection.close()
        db_connection = None

#mock data 
def initialize_database():

    global db_connection
    cursor = db_connection.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS redis_keys (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    data = [
        ('auger_pivot_angle', '40'),
        ('auger_pivot_angle_max', '90'),
        ('auger_pivot_angle_min', '0'),
        ('auger_fold_angle', '40'),
        ('auger_fold_angle_min', '0'),
        ('auger_fold_angle_max', '90'),
        ('spout_tilt_angle', '40'),
        ('spout_tilt_angle_min', '0'),
        ('spout_tilt_angle_max', '90'),
        ('spout_rotation_angle', '45'),
        ('spout_rotation_angle_max', '180'),
        ('spout_rotation_angle_min', '90'),
        ('gate_angle', '50'),
        ('gate_angle_max', '90'),
        ('gate_angle_min', '0'),
        ('auger_pivot_speed_ref', '30'),
        ('auger_fold_speed_ref', '30'),
        ('spout_tilt_speed_ref', '30'),
        ('spout_rotation_speed_ref', '30'),
        ('gate_speed_ref', '30'),
        ('simulation_power', 'true')
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO redis_keys (key, value) VALUES (?, ?)", data
    )

    db_connection.commit()

    if db_connection is None:
        raise ConnectionError("SQLite database connection is not established!")

    print("Database initialized successfully with mock data!")