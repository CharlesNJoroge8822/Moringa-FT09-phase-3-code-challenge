import sqlite3
import os

DATABASE_NAME = './database/magazine.db'

# Check if the directory exists, create it if not
if not os.path.exists(os.path.dirname(DATABASE_NAME)):
    os.makedirs(os.path.dirname(DATABASE_NAME))

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

