from sqlite_db.questions_db import get_question
from .db_functions import connect_db

conn, cursor = connect_db()

def add_answer(question_id, user_id, answer, poll_id):
    cursor.execute(
        'SELECT answer FROM question_answers WHERE user_id = ? AND question_id = ?',
        (user_id, question_id)
    )
    if len(cursor.fetchall()) == 0:
        cursor.execute(
            'INSERT INTO question_answers (question_id, user_id, answer, poll_id) VALUES (?, ?, ?, ?)',
            (question_id, user_id, answer, poll_id)
        )
    else:
        cursor.execute(
            'UPDATE question_answers SET answer = ? WHERE user_id = ? AND question_id = ?',
            (answer, user_id, question_id)
        )
    conn.commit()
    
def send_answered_poll(user_id, poll_id):
    cursor.execute(
        'UPDATE poll_answers SET status = ? WHERE user_id = ? AND poll_id = ?',
        ('answered', user_id, poll_id)
    )
    conn.commit()
    
def get_answered_polls():
    cursor.execute(
        'SELECT poll_id FROM poll_answers WHERE status = ?',
        ('answered',)
    )
    return cursor.fetchall()

def get_users(poll_id):
    cursor.execute(
        'SELECT user_id FROM poll_answers WHERE poll_id = ? AND status = ?',
        (poll_id, 'answered')
    )
    return cursor.fetchall()


def get_answers(user_id, poll_id):
    cursor.execute(
        'SELECT answer, question_id FROM question_answers WHERE user_id = ? AND poll_id = ? ORDER BY question_id',
        (user_id, poll_id)
    )
    answers_list = []
    for answer in cursor.fetchall():
        answers_list.append((get_question(question_id=answer[1]), answer[0]))
    return answers_list

def get_answer(question_id, user_id):
    cursor.execute(
        'SELECT answer FROM question_answers WHERE question_id = ? AND user_id = ?',
        (question_id, user_id)
    )
    return cursor.fetchall()

def send_poll(user_id, poll_id):
    try:
        cursor.execute(
            'INSERT INTO poll_answers (user_id, poll_id, status) VALUES (?, ?, ?)',
            (user_id, poll_id, 'not_answered')
        )
    except:
        pass
    conn.commit()
    

def get_polls_ids(user_id) -> list:
    cursor.execute(
        'SELECT poll_id FROM poll_answers WHERE status = ? AND user_id = ?',
        ('not_answered', user_id)
    )
    return cursor.fetchall()