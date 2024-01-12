from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from enums import CallBacks, ButtonsText

main_menu_kb = [
    [InlineKeyboardButton(text=ButtonsText.main_menu.value, callback_data=CallBacks.main_menu.value)]
]
main_menu_mk = InlineKeyboardMarkup(inline_keyboard=main_menu_kb)

accept_kb = [
    [InlineKeyboardButton(text=ButtonsText.yes.value, callback_data=CallBacks.accept.value),
     InlineKeyboardButton(text=ButtonsText.no.value, callback_data=CallBacks.reject.value)]
]
accept_mk = InlineKeyboardMarkup(inline_keyboard=accept_kb)

# def back_mk_generator(clbck):
#     back_kb = [
#         [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=clbck)]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=back_kb)
# reply_markup=common_keyboards.back_mk_generator(f'{CallBacks.poll_id_prefix.value}{CallBacks.prefix_divider.value}{clbck_data}'

back_kb = [
    [InlineKeyboardButton(text=ButtonsText.back.value, callback_data=CallBacks.reject.value)]
]
back_mk = InlineKeyboardMarkup(inline_keyboard=back_kb)