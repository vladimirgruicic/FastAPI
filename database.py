import sqlite3
from sqlite3 import Connection

# Connection for the database.
def connect_to_database():
    conn = sqlite3.connect('data/fastapi.db')
    return conn

# Initialization of the database.
def initialize_database():
    conn = connect_to_database()
    cursor = conn.cursor()

    # Create items table.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL,
            quantity INTEGER
        )
    ''')

    # Create user table.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            user_request TEXT NOT NULL    
        )
    ''')

    conn.commit()
    conn.close()


# Getting the connection for database to pass it into main.py or other files to work with database.
def get_db() -> Connection:
    db = connect_to_database()
    return db