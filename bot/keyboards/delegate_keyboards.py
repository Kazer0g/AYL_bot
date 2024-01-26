from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from sqlite_db import questions_db
from enums import ButtonsText, CallBacks
from enums import DialogStatuses

def answer_mk_generator(poll_id):
    answer_kb = [
        [InlineKeyboardButton(text=ButtonsText.answer.value, callback_data=f'{CallBacks.answer.value}{CallBacks.divider.value}{poll_id}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=answer_kb)

def poll_list_mk_generator(poll_id):
    questions = questions_db.get_questions(poll_id=poll_id)
    poll_list = [
        
    ]
    for question_id_db in questions:
        question_id = question_id_db[0]
        question = questions_db.get_question(question_id=question_id)
        
        poll_list.append(
            [InlineKeyboardButton(text=question, callback_data=f'{CallBacks.question.value}{CallBacks.divider.value}{question_id}')]
        )
    poll_list.append(
        [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
    )
    return InlineKeyboardMarkup(inline_keyboard=poll_list)