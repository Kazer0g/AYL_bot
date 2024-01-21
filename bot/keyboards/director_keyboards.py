from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import ButtonsText, CallBacks
from sqlite_db import users_db, polls_db, questions_db

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

def polls_list_mk_generator ():
    polls = polls_db.get_polls()
    polls_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.add_poll.value, callback_data=CallBacks.add_poll.value)],
        
    ]
    for poll in polls:
        poll_id = poll[0]
        poll_name = polls_db.get_poll_name(poll_id=poll_id)
        polls_list.append([InlineKeyboardButton(text=f'{poll_name} id:{str(poll_id)}', callback_data=f'{CallBacks.poll_id_prefix.value}{CallBacks.prefix_divider.value}{poll_id}')])
                          
    polls_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=polls_list)

def poll_list_mk_generator (poll_id):
    questions = questions_db.get_questions(poll_id=poll_id)
    print (questions)
    poll_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value),
        InlineKeyboardButton(text=ButtonsText.polls.value, callback_data=CallBacks.polls.value)],
        [InlineKeyboardButton(text=polls_db.get_poll_name(poll_id=poll_id), callback_data=f'{CallBacks.poll_name_prefix.value}{CallBacks.prefix_divider.value}{poll_id}'),
         InlineKeyboardButton(text=polls_db.get_poll_type(poll_id=poll_id), callback_data=f'{CallBacks.poll_type_prefix.value}{CallBacks.prefix_divider.value}{poll_id}')],
        [InlineKeyboardButton(text=ButtonsText.delete.value, callback_data=f'{CallBacks.delete_poll_prefix.value}{CallBacks.prefix_divider.value}{poll_id}'),
         InlineKeyboardButton(text=ButtonsText.send_poll.value, callback_data=f'{CallBacks.send_poll.value}{CallBacks.prefix_divider.value}{poll_id}')],
        [InlineKeyboardButton(text=ButtonsText.add_question.value, callback_data=f'{CallBacks.add_question_prefix.value}{CallBacks.prefix_divider.value}{poll_id}')],
    ]
    for question_id_db in questions:
        question_id = question_id_db[0]
        question = questions_db.get_question(question_id=question_id)
        
        poll_list.append(
            [InlineKeyboardButton(text=question, callback_data=f'{CallBacks.question_prefix.value}{CallBacks.prefix_divider.value}{question_id}'),
             InlineKeyboardButton(text=ButtonsText.delete.value, callback_data=f'{CallBacks.delete_question_prefix.value}{CallBacks.prefix_divider.value}{question_id}')]
        )
    
    poll_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=poll_list)

poll_types_kb = [
    [InlineKeyboardButton(text=ButtonsText.thread_1.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.prefix_divider.value}{CallBacks.thread_1.value}'),
     InlineKeyboardButton(text=ButtonsText.thread_2.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.prefix_divider.value}{CallBacks.thread_2.value}'),
     InlineKeyboardButton(text=ButtonsText.thread_3.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.prefix_divider.value}{CallBacks.thread_3.value}')],
    [InlineKeyboardButton(text=ButtonsText.thread_junior.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.prefix_divider.value}{CallBacks.thread_junior.value}'),
     InlineKeyboardButton(text=ButtonsText.thread_global.value, callback_data=f'{CallBacks.thread_prefix.value}{CallBacks.prefix_divider.value}{CallBacks.thread_global.value}')],
     [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
]
poll_types_mk = InlineKeyboardMarkup(inline_keyboard=poll_types_kb)

# question_types_kb = [
#     [InlineKeyboardButton(text=ButtonsText.question_type_text.value, callback_data=)],
#     [InlineKeyboardButton(text=ButtonsText.question_type_1_5.value, callback_data=),
#      InlineKeyboardButton(text=ButtonsText.question_type_1_10.value, callback_data=)]
# ]
# question_types_mk = InlineKeyboardMarkup(inline_keyboard=question_types_kb)