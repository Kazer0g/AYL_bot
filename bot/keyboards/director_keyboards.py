from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import ButtonsText, CallBacks
from sqlite_db import db_functions

main_menu_kb = [
    [InlineKeyboardButton(text=ButtonsText.presenters.value, callback_data=CallBacks.presenters.value)],
    [InlineKeyboardButton(text=ButtonsText.send_poll.value, callback_data=CallBacks.send_poll.value)],
    [InlineKeyboardButton(text=ButtonsText.feedback.value, callback_data=CallBacks.feedback.value)]
]
main_menu_mk = InlineKeyboardMarkup(inline_keyboard=main_menu_kb)


def staff_list_mk_generator ():
    staff = db_functions.get_staff()
    staff_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.add_person.value, callback_data=CallBacks.add_person.value)],
        
    ]
    for staff_id in staff:
        user_id = staff_id[0]
        username = db_functions.get_username(user_id=user_id)
        role = db_functions.get_role(user_id=user_id)
        staff_list.append([InlineKeyboardButton(text=username, callback_data=f'{CallBacks.username_prefix.value}{CallBacks.prefix_divider.value}{username}'),
                           InlineKeyboardButton(text=role, callback_data=f'{CallBacks.role_prefix.value}{CallBacks.prefix_divider.value}{role}{CallBacks.data_divider.value}{username}'),
                           InlineKeyboardButton(text='-', callback_data=f'{CallBacks.delete_stuff_prefix.value}{CallBacks.prefix_divider.value}{username}')])
    staff_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=staff_list)

def polls_list_mk_generator ():
    polls = db_functions.get_polls()
    polls_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.add_poll.value, callback_data=CallBacks.add_poll.value)],
        
    ]
    for poll in polls:
        poll_id = poll[0]
        poll_name = db_functions.get_poll_name(poll_id=poll_id)
        polls_list.append([InlineKeyboardButton(text=str(poll_id), callback_data=f'{CallBacks.poll_id_prefix.value}{CallBacks.prefix_divider.value}{poll_id}'),
                           InlineKeyboardButton(text=poll_name, callback_data=f'{CallBacks.poll_name_prefix.value}{CallBacks.prefix_divider.value}{poll_name}'),
                           InlineKeyboardButton(text='-', callback_data=f'{CallBacks.delete_poll_prefix.value}{CallBacks.prefix_divider.value}{poll_id}')])
    polls_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=polls_list)

def poll_list_mk_generator ():
    # polls = db_functions.get_polls()
    # print (polls)
    poll_list = [
        [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
        [InlineKeyboardButton(text=ButtonsText.polls.value, callback_data=CallBacks.send_poll.value)],
        [InlineKeyboardButton(text=ButtonsText.add_question.value, callback_data=CallBacks.add_question.value)],
        
    ]
    # for poll_id in polls:
    #     user_id = staff_id[0]
    #     username = db_functions.get_username(user_id=user_id)
    #     role = db_functions.get_role(user_id=user_id)
    #     staff_list.append([InlineKeyboardButton(text=username, callback_data=f'{CallBacks.username_prefix.value}{CallBacks.prefix_divider.value}{username}'),
    #                        InlineKeyboardButton(text=role, callback_data=f'{CallBacks.role_prefix.value}{CallBacks.prefix_divider.value}{role}{CallBacks.data_divider.value}{username}'),
    #                        InlineKeyboardButton(text='-', callback_data=f'{CallBacks.delete_prefix.value}{CallBacks.prefix_divider.value}{username}')])
    poll_list.append(
        [InlineKeyboardButton(text="<", callback_data="previous"), 
         InlineKeyboardButton(text='&&&', callback_data='page'),
         InlineKeyboardButton(text='>', callback_data='next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=poll_list)