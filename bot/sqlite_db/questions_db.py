from enums import Statuses
from .db_functions import connect_db

conn, cursor = connect_db()

def add_question(poll_id):
    cursor.execute(
        'INSERT INTO questions (poll_id) VALUES (?)',
        (poll_id,)
    )
    cursor.execute(
        'SELECT last_insert_rowid()',
    )
    question_id = cursor.fetchall()[0][0]
    conn.commit()
    return question_id

def get_question(question_id):
    cursor.execute(
        'SELECT question FROM questions WHERE question_id = ?',
        (question_id,)
    )
    return cursor.fetchall()[0][0]

def get_questions(poll_id):
    cursor.execute(
        'SELECT question_id FROM questions WHERE poll_id = ?',
        (poll_id,)
    )
    return cursor.fetchall()

def set_question(question_id, question):
    cursor.execute(
        'UPDATE questions SET question = ? WHERE question_id = ?',
        (question, question_id)
    )
    conn.commit()