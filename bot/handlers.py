import texts
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from enums import CallBacks, DialogStatuses, Roles, Texts
from keyboards import common_keyboards, director_keyboards
from sqlite_db import add_user, get_role

# from validators import

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    role = add_user(user_id=msg.from_user.id, username=msg.from_user.username, role=Roles.delegate.value)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            await msg.answer(texts.GREETINGS_FOR_DIRECTOR, reply_markup=common_keyboards.main_menu_mk)

@router.callback_query(F.data == CallBacks.main_menu.value)
async def main_menu_reply_handler(clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            await clbck.message.edit_text(Texts.main_menu.value)
            await clbck.message.edit_reply_markup(reply_markup=director_keyboards.main_menu_mk)
