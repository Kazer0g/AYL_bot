from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import ButtonsText, CallBacks
from enums import DialogStatuses
from sqlite_db import users_db, polls_db, questions_db, get_question, get_question_type, get_answered_polls, get_users, get_username

main_menu_kb = [
    [InlineKeyboardButton(text=ButtonsText.presenters.value, callback_data=CallBacks.presenters.value)],
    [InlineKeyboardButton(text=ButtonsText.polls.value, callback_data=CallBacks.polls.value)],
    [InlineKeyboardButton(text=ButtonsText.feedback.value, callback_data=CallBacks.feedback.value)]
]
main_menu_mk = InlineKeyboardMarkup(inline_keyboard=main_menu_kb)


def staff_list_mk_generator ():
    staff = users_db.get_staff()
    staff_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.add_person.value, callback_data=CallBacks.add_person.value)],
        
    ]
    for staff_id in staff:
        user_id = staff_id[0]
        username = users_db.get_username(user_id=user_id)
        role = users_db.get_role(user_id=user_id)
        staff_list.append([InlineKeyboardButton(text=username, callback_data=f'{CallBacks.username_prefix.value}{CallBacks.prefix_divider.value}{username}'),
                           InlineKeyboardButton(text=role, callback_data=f'{CallBacks.role_prefix.value}{CallBacks.prefix_divider.value}{role}{CallBacks.data_divider.value}{username}'),
                           InlineKeyboardButton(text=ButtonsText.delete.value, callback_data=f'{CallBacks.delete_stuff_prefix.value}{CallBacks.prefix_divider.value}{username}')])
    staff_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=staff_list)

def feedback_list_mk_generator():
    feedback_list_kb = [[InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)]]

    polls_ids = get_answered_polls()
    for poll_id in polls_ids:
        poll_id = poll_id[0]
        poll_name = polls_db.get_poll_name(poll_id=poll_id)
        feedback_list_kb.append([InlineKeyboardButton(text=poll_name, callback_data=f'{CallBacks.poll.value}{CallBacks.divider.value}{poll_id}')])
                          
    feedback_list_kb.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )

    return InlineKeyboardMarkup(inline_keyboard=feedback_list_kb)

def feedback_users_list_mk_generator(poll_id):
    users_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.feedback.value)]
    ]
    users_ids = get_users(poll_id=poll_id)
    for user_id in users_ids:
        id = user_id[0]
        users_list.append(
            [InlineKeyboardButton(text=get_username(user_id=id), callback_data=f'{CallBacks.answer.value}{CallBacks.divider.value}{poll_id}{CallBacks.spliter.value}{id}')]
        )
        
    return InlineKeyboardMarkup(inline_keyboard=users_list)

def polls_list_mk_generator ():
    polls = polls_db.get_polls()
    polls_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.add_poll.value, callback_data=CallBacks.add_poll.value)],
        
    ]
    for poll in polls:
        poll_id = poll[0]
        poll_name = polls_db.get_poll_name(poll_id=poll_id)
        polls_list.append([InlineKeyboardButton(text=f'{poll_name} id:{str(poll_id)}', callback_data=f'{CallBacks.poll.value}{CallBacks.divider.value}{poll_id}')])
                          
    polls_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=polls_list)

def poll_list_mk_generator (poll_id):
    questions = questions_db.get_questions(poll_id=poll_id)
    poll_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value),
        InlineKeyboardButton(text=ButtonsText.polls.value, callback_data=CallBacks.polls.value)],
        [InlineKeyboardButton(text=polls_db.get_poll_name(poll_id=poll_id), callback_data=CallBacks.poll_name.value),
         InlineKeyboardButton(text=polls_db.get_poll_type(poll_id=poll_id), callback_data=CallBacks.poll_type.value)],
        [InlineKeyboardButton(text=ButtonsText.delete.value, callback_data=CallBacks.delete.value),
         InlineKeyboardButton(text=ButtonsText.send_poll.value, callback_data=CallBacks.send_poll.value)],
        [InlineKeyboardButton(text=ButtonsText.add_question.value, callback_data=CallBacks.add_question.value)],
    ]
    for question_id_db in questions:
        question_id = question_id_db[0]
        question = questions_db.get_question(question_id=question_id)
        
        poll_list.append(
            [InlineKeyboardButton(text=question, callback_data=f'{CallBacks.question.value}{CallBacks.divider.value}{question_id}')]
        )
        # InlineKeyboardButton(text=ButtonsText.delete.value, callback_data=CallBacks.delete.value)
    
    poll_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=poll_list)

def question_list_mk_generator (question_id):
    question_list_kb = [
        [InlineKeyboardButton(text=ButtonsText.change_question.value, callback_data=CallBacks.change_question.value),
         InlineKeyboardButton(text=get_question_type(question_id = question_id), callback_data=CallBacks.change_question_type.value)],
        [InlineKeyboardButton(text=ButtonsText.back_to_poll.value, callback_data=f'{CallBacks.poll.value}{CallBacks.divider.value}{questions_db.get_poll_id(question_id=question_id)}'),
         InlineKeyboardButton(text=ButtonsText.delete.value, callback_data=CallBacks.delete.value)],
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=question_list_kb)

poll_types_kb = [
    [InlineKeyboardButton(text=ButtonsText.thread_1.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.divider.value}{CallBacks.thread_1.value}'),
     InlineKeyboardButton(text=ButtonsText.thread_2.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.divider.value}{CallBacks.thread_2.value}'),
     InlineKeyboardButton(text=ButtonsText.thread_3.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.divider.value}{CallBacks.thread_3.value}')],
    [InlineKeyboardButton(text=ButtonsText.thread_junior.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.divider.value}{CallBacks.thread_junior.value}'),
     InlineKeyboardButton(text=ButtonsText.thread_global.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.divider.value}{CallBacks.thread_global.value}')],
     [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
]
poll_types_mk = InlineKeyboardMarkup(inline_keyboard=poll_types_kb)

question_types_kb = [
    [InlineKeyboardButton(text=ButtonsText.question_type_text.value, callback_data=f'{CallBacks.set_question_type.value}{CallBacks.divider.value}{CallBacks.question_type_text.value}')],
    [InlineKeyboardButton(text=ButtonsText.question_type_1_5.value, callback_data=f'{CallBacks.set_question_type.value}{CallBacks.divider.value}{CallBacks.question_type_1_5.value}'),
     InlineKeyboardButton(text=ButtonsText.question_type_1_10.value, callback_data=f'{CallBacks.set_question_type.value}{CallBacks.divider.value}{CallBacks.question_type_1_10.value}')],
    [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
]
question_types_mk = InlineKeyboardMarkup(inline_keyboard=question_types_kb)