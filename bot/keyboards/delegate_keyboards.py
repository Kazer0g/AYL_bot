from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from sqlite_db import questions_db, answers_db
from enums import ButtonsText, CallBacks

def answer_mk_generator(poll_id):
    answer_kb = [
        [InlineKeyboardButton(text=ButtonsText.answer.value, callback_data=f'{CallBacks.take.value}{CallBacks.divider.value}{poll_id}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=answer_kb)

def poll_list_mk_generator(poll_id, user_id):
    flag = True
    questions = questions_db.get_questions(poll_id=poll_id)
    poll_list = [
        
    ]
    for question_id_db in questions:
        question_id = question_id_db[0]
        question = questions_db.get_question(question_id=question_id)
        if len(answers_db.get_answer(question_id=question_id, user_id=user_id)) > 0:
            question += ' +'
        else:
            question += ' -'
            flag = False
        poll_list.append(
            [InlineKeyboardButton(text=question, callback_data=f'{CallBacks.question.value}{CallBacks.divider.value}{question_id}')]
        )
    if flag:
        poll_list.append(
            [InlineKeyboardButton(text=ButtonsText.send_poll.value, callback_data=CallBacks.send_poll.value)]
        )
    poll_list.append(
        [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
    )
    return InlineKeyboardMarkup(inline_keyboard=poll_list)
def type_1_5_mk_generator(question_id):
    
    type_1_5_kb = []
    for i in range(5):
        type_1_5_kb.append([InlineKeyboardButton(text=str(i+1), callback_data=f'{CallBacks.answer.value}{CallBacks.divider.value}{i+1}{CallBacks.spliter.value}{question_id}')])
    type_1_5_kb.append(
        [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
    )
    return InlineKeyboardMarkup(inline_keyboard=type_1_5_kb)

def type_1_10_mk_generator(question_id):
    
    type_1_10_kb = []
    for i in range(10):
        type_1_10_kb.append([InlineKeyboardButton(text=str(i+1), callback_data=f'{CallBacks.answer.value}{CallBacks.divider.value}{i+1}{CallBacks.spliter.value}{question_id}')])
    type_1_10_kb.append(
        [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
    )
    return InlineKeyboardMarkup(inline_keyboard=type_1_10_kb)
