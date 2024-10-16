# app/db_service.py
import sqlite3

connection = None

def connect_db(db_name: str):
    global connection
    connection = sqlite3.connect(db_name)

def disconnect_db():
    global connection
    if connection:
        connection.close()
        connection = None
