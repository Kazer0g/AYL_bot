from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import CallBacks

main_menu_kb = [
    [InlineKeyboardButton(text='Ведущие', callback_data=CallBacks.presenters.value)],
    [InlineKeyboardButton(text='Отправить анкету', callback_data=CallBacks.send_poll.value)],
    [InlineKeyboardButton(text='Посмотреть обратную связь', callback_data=CallBacks.feedback.value)]
]
main_menu_mk = InlineKeyboardMarkup(inline_keyboard=main_menu_kb)