import texts
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from enums import CallBacks, DialogStatuses, MenuTexts, Roles
from keyboards import common_keyboards, director_keyboards
from sqlite_db import add_user, get_role, set_dialog_status

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
    set_dialog_status(user_id=msg.from_user.id, dialog_status=DialogStatuses.none.value)

@router.callback_query(F.data == CallBacks.main_menu.value)
async def main_menu_reply_handler(clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            await clbck.message.edit_text(text=MenuTexts.main_menu.value)
            await clbck.message.edit_reply_markup(reply_markup=director_keyboards.main_menu_mk)

@router.callback_query(F.data == CallBacks.send_poll.value)
async def send_poll_reply_handler(clbck: CallbackQuery):
    pass

@router.callback_query(F.data == CallBacks.presenters.value)
async def presenters_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.presenters.value)
    staff_list_mk = director_keyboards.staff_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=staff_list_mk)


@router.callback_query(F.data == CallBacks.feedback.value)
async def feedback_reply_handler(clbk: CallbackQuery):
    pass

@router.callback_query(F.data == F.data)
async def custom_reply_handler(clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            clbck_prefix, clbck_data = clbck.data.split(CallBacks.prefix_divider.value)
            match clbck_prefix:
                case CallBacks.username_prefix.value:
                    pass
                case CallBacks.role_prefix.value:
                    pass
                case CallBacks.delete_prefix.value:
                    await clbck.message.answer(text=texts.delete_from_stuff_message_generator(username=clbck_data, role=Roles.delegate.value))