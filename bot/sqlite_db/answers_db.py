from .db_functions import connect_db

conn, cursor = connect_db()

def add_answer(question_id, user_id, answer, poll_id):
    cursor.execute(
        'INSERT INTO question_answers (question_id, user_id, answer, poll_id) VALUES (?, ?, ?, ?)',
        (question_id, user_id, answer, poll_id)
    )
    conn.commit()

def get_answer(question_id, user_id):
    cursor.execute(
        'SELECT answer FROM question_answers WHERE question_id = ? AND user_id = ?',
        (question_id, user_id)
    )
    return cursor.fetchall()