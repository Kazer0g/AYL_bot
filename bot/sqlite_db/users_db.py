import sqlite3
from enums import Statuses
from .db_functions import connect_db

conn, cursor = connect_db()

def add_user (user_id, mode, username):
    print (user_id, username)
    try:
        cursor.execute(
            'INSERT INTO users (username, user_id, mode) VALUES (?, ?, ?)',
            (username, user_id, mode)
        )
        conn.commit()
        return get_role(user_id=user_id)
    except sqlite3.IntegrityError:
        cursor.execute(
            'UPDATE users SET status = ? AND mode = ? WHERE user_id = ?', 
            (Statuses.status_active.value, mode, user_id)
        )

        cursor.execute(
            'SELECT conference_role FROM users WHERE user_id = ?',
            (user_id,)
        )
        conn.commit()
        return cursor.fetchall()[0][0]

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
        'SELECT user_id FROM users WHERE conference_status = "active" AND conference_role != "delegate" AND conference_role != "director"'    )
    return cursor.fetchall()

def get_dialog_status(user_id) -> str:
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
    
def get_delegates(thread):
    match thread:
        case Statuses.thread_global.value:
            cursor.execute(
                'SELECT user_id FROM users WHERE conference_role = ? AND conference_status = ?',
                ('delegate', 'active')
            )
            return cursor.fetchall()