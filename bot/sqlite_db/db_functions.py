import sqlite3
from enums import Statuses


def connect_db ():
    db_path = 'bot/sqlite_db/db.db'
    conn = sqlite3.connect(db_path)
    cursor= conn.cursor()
    
    return conn, cursor