import logging
import sqlite3
from enums import Statuses
from .db_functions import connect_db

conn, cursor = connect_db()

def add_poll(user_id):
    cursor.execute(
        'INSERT INTO polls (creator_id) VALUES (?);',
        (user_id,)
    )
    cursor.execute(
        'SELECT last_insert_rowid()',
    )
    conn.commit()
    return cursor.fetchall()[0][0]

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

def set_poll_name(poll_id, poll_name):
    cursor.execute(
        'UPDATE polls SET poll_name = ? WHERE poll_id = ?',
        (poll_name, poll_id)
    )
    conn.commit()

def get_poll_type(poll_id):
    cursor.execute(
        'SELECT poll_type FROM polls WHERE poll_id = ?',
        (poll_id,)
    )
    return cursor.fetchall()[0][0]

def set_poll_type(poll_id, poll_type):
    cursor.execute(
        'UPDATE polls SET poll_type = ? WHERE poll_id = ?',
        (poll_type, poll_id)
    )
    conn.commit()

def delete_poll(poll_id):
    cursor.execute(
        'DELETE FROM polls WHERE poll_id = ?;',
        (poll_id,)
    )
    conn.commit()