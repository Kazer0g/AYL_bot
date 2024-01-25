from enums import Statuses
from .db_functions import connect_db

conn, cursor = connect_db()


def add_question(poll_id):
    cursor.execute("INSERT INTO questions (poll_id) VALUES (?)", (poll_id,))
    cursor.execute(
        "SELECT last_insert_rowid()",
    )
    question_id = cursor.fetchall()[0][0]
    conn.commit()
    return question_id


def get_question(question_id):
    cursor.execute(
        "SELECT question FROM questions WHERE question_id = ?", (question_id,)
    )
    return cursor.fetchall()[0][0]


def get_question_type(question_id):
    cursor.execute("SELECT type FROM questions WHERE question_id = ?", (question_id,))
    return cursor.fetchall()[0][0]


def get_poll_id(question_id):
    print(question_id, "9" * 10)
    cursor.execute(
        "SELECT poll_id FROM questions WHERE question_id = ?", (question_id,)
    )
    return cursor.fetchall()[0][0]


def get_questions(poll_id):
    cursor.execute("SELECT question_id FROM questions WHERE poll_id = ?", (poll_id,))
    return cursor.fetchall()


def set_question(question_id, question):
    cursor.execute(
        "UPDATE questions SET question = ? WHERE question_id = ?",
        (question, question_id),
    )
    conn.commit()


def set_question_type(question_id, question_type):
    cursor.execute(
        "UPDATE questions SET type = ? WHERE question_id = ?",
        (question_type, question_id),
    )
    conn.commit()


def delete_question(question_id):
    poll_id = get_poll_id(question_id=question_id)
    cursor.execute("DELETE FROM questions WHERE question_id = ?", (question_id,))
    conn.commit()
    return poll_id
