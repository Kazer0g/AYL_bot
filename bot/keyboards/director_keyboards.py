from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import CallBacks, ButtonsText

main_menu_kb = [
    [InlineKeyboardButton(text=ButtonsText.presenters.value, callback_data=CallBacks.presenters.value)],
    [InlineKeyboardButton(text=ButtonsText.send_poll.value, callback_data=CallBacks.send_poll.value)],
    [InlineKeyboardButton(text=ButtonsText.feedback.value, callback_data=CallBacks.feedback.value)]
]
main_menu_mk = InlineKeyboardMarkup(inline_keyboard=main_menu_kb)

staff_list_kb = [
    [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)],
    [InlineKeyboardButton(text=ButtonsText.add_person.value, callback_data=CallBacks.add_person.value)],
    
]
staff_list_mk = InlineKeyboardMarkup(inline_keyboard=staff_list_kb)