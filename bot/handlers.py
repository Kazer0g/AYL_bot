import texts
from aiogram import F, Router, exceptions
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from enums import CallBacks, DialogStatuses, MenuTexts, Roles
from keyboards import common_keyboards, director_keyboards
from sqlite_db import (
    add_poll,
    add_user,
    get_polls,
    get_role,
    set_dialog_status,
    set_main_message_id,
    get_dialog_status,
    delete_poll,
    get_main_message_id,
)

# from validators import

router = Router()

async def message_deleter(msg: Message, main_message_id):
    try:
        message_id = msg.message_id
        while message_id > main_message_id:
                print (message_id)
                try:
                    await msg.bot.delete_message(chat_id=msg.chat.id, message_id=message_id)
                except:
                    pass
                message_id -= 1
    except exceptions.TelegramBadRequest:
        message_deleter(msg)

@router.message(Command("start"))
async def start_handler(msg: Message):
    set_main_message_id(user_id=msg.from_user.id, message_id=msg.message_id)
    await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
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
    await clbck.message.edit_text(text=MenuTexts.polls.value)
    polls_list_mk = director_keyboards.polls_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=polls_list_mk)

@router.callback_query(F.data == CallBacks.add_poll.value)
async def add_poll_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.poll.value)
    poll_list_mk = director_keyboards.poll_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=poll_list_mk)
    add_poll(user_id=clbck.from_user.id)

@router.callback_query(F.data == CallBacks.presenters.value)
async def presenters_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.presenters.value)
    staff_list_mk = director_keyboards.staff_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=staff_list_mk)


@router.callback_query(F.data == CallBacks.feedback.value)
async def feedback_reply_handler(clbk: CallbackQuery):
    pass

@router.callback_query(F.data == CallBacks.accept.value)
async def accepr_reply_handler (clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            dialog_prefix, dialog_data = get_dialog_status(user_id=clbck.from_user.id).split(CallBacks.prefix_divider.value)
            match dialog_prefix:
                case CallBacks.username_prefix.value:
                    pass
                case CallBacks.role_prefix.value:
                    pass
                case CallBacks.delete_stuff_prefix.value:
                    pass    
                case CallBacks.poll_id_prefix.value:
                    pass
                case CallBacks.poll_name_prefix.value:
                    pass
                case CallBacks.delete_poll_prefix.value:
                    delete_poll(poll_id=dialog_data)
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(clbck.from_user.id))
                    await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.polls_list_mk_generator())
                    

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
                case CallBacks.delete_stuff_prefix.value:
                    await clbck.message.answer(text=texts.delete_from_stuff_message_generator(username=clbck_data, role=Roles.delegate.value), reply_markup=common_keyboards.accept_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{CallBacks.delete_stuff_prefix.value}{CallBacks.prefix_divider.value}{clbck_data}')
                case CallBacks.poll_id_prefix.value:
                    pass
                case CallBacks.poll_name_prefix.value:
                    pass
                case CallBacks.delete_poll_prefix.value:
                    await clbck.message.answer(text=texts.delete_from_polls_message_generator(poll_name=clbck_data), reply_markup=common_keyboards.accept_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{CallBacks.delete_poll_prefix.value}{CallBacks.prefix_divider.value}{clbck_data}')
