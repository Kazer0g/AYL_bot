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
            'INSERT INTO users (username, user_id, status, conference_role, static_role) VALUES (?, ?, ?, ?, ?)',
            (username, user_id, Statuses.status_active.value, role, role)
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
            'SELECT conference_role FROM users WHERE user_id = ?',
            (user_id,)
        )
        conn.commit()
        return cursor.fetchall()[0][0]

def add_poll(user_id):
    cursor.execute(
        'INSERT INTO polls (creator_id) VALUES (?)',
        (user_id,)
    )
    conn.commit()
    logging.info(f'{get_username(user_id=user_id)} created poll')

def get_mode(user_id):
    cursor.execute(
        'SELECT mode FROM users WHERE user_id = ?',
        (user_id,)
    )
    return cursor.fetchall()[0][0]

def get_role(user_id):
    mode = get_mode(user_id=user_id)
    match mode:
        case Statuses.static_mode.value:
            cursor.execute(
                'SELECT static_role FROM users WHERE user_id = ?',
                (user_id,)
            )
        case Statuses.conference_mode.value:
            cursor.execute(
                'SELECT conference_role FROM users WHERE user_id = ?',
                (user_id,)
            )
    return cursor.fetchall()[0][0]

def get_username(user_id):
    cursor.execute(
        'SELECT username FROM users WHERE user_id = ?',
        (user_id,)
    )
    return cursor.fetchall()[0][0]

def get_staff():
    cursor.execute(
        'SELECT user_id FROM users WHERE status = "active"'
    )
    return cursor.fetchall()

def get_polls():
    cursor.execute(
        'SELECT poll_id FROM polls'
    )
    return cursor.fetchall()

def get_poll_name(poll_id):
    cursor.execute(
        'SELECT poll_name FROM polls WHERE poll_id = ?',
        (poll_id,)
    )
    return cursor.fetchall()[0][0]

def delete_poll(poll_id):
    cursor.execute(
        'DELETE FROM polls WHERE poll_id = ?',
        (poll_id,)
    )
    conn.commit()

def get_dialog_status(user_id):
    cursor.execute(
        'SELECT dialog_status FROM users WHERE user_id = ?',
        (user_id,)    
        )
    return cursor.fetchall()[0][0]

def set_dialog_status(user_id, dialog_status):
    cursor.execute(
        'UPDATE users SET dialog_status = ? WHERE user_id = ?',
        (dialog_status, user_id)
    )
    conn.commit()
    username = get_username(user_id=user_id)
    logging.info(f'{username} dialog status changed: {dialog_status}')

def get_main_message_id (user_id):
    cursor.execute(
        'SELECT main_message_id FROM users WHERE user_id = ?',
        (user_id,)
    )
    return cursor.fetchall()[0][0]

def set_main_message_id (user_id, message_id):
    cursor.execute(
        'UPDATE users SET main_message_id = ? WHERE user_id = ?',
        (message_id+1, user_id)
    )