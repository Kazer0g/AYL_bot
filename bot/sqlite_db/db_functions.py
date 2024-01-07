import logging
import sqlite3
from enums import Statuses

def connect_db (db_path: str):
    global conn, cursor
    conn = sqlite3.connect(db_path)
    logging.info('Database connected')
    cursor = conn.cursor()

def add_user (username, user_id, role):
    try:
        cursor.execute(
            'INSERT INTO users (username, user_id, status, role) VALUES (?, ?, ?, ?)',
            (username, user_id, Statuses.status_active.value, role)
        )
        conn.commit()
        logging.info (f'Added username:{username}, user_id:{user_id}')
        return role
    except sqlite3.IntegrityError:
        cursor.execute(
            'UPDATE users SET status = ? WHERE user_id = ?', 
            (Statuses.status_active.value, user_id)
        )
        logging.info(f'Record with username:{username} and user_id:{user_id} is already exists, status = active')
        cursor.execute(
            'SELECT role FROM users WHERE user_id = ?',
            (user_id,)
        )
        conn.commit()
        return cursor.fetchall()[0][0]
    
def get_role(user_id):
    cursor.execute(
        'SELECT role FROM users WHERE user_id = ?',
        (user_id,)
    )
    return cursor.fetchall()[0][0]