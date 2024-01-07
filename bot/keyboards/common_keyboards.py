from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import CallBacks

main_menu_kb = [
    [InlineKeyboardButton(text='В главное меню', callback_data=CallBacks.main_menu.value)]
]
main_menu_mk = InlineKeyboardMarkup(inline_keyboard=main_menu_kb)