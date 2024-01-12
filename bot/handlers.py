import texts
from aiogram import F, Router, exceptions
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from enums import CallBacks, DialogStatuses, MenuTexts, Roles, Statuses
from keyboards import common_keyboards, director_keyboards
from sqlite_db import (
    add_poll,
    add_user,
    delete_poll,
    get_dialog_status,
    get_main_message_id,
    get_poll_name,
    get_polls,
    get_role,
    set_dialog_status,
    set_main_message_id,
    set_poll_type,
    set_poll_name,
)

# from validators import

router = Router()

async def message_deleter(msg: Message, main_message_id):
    try:
        message_id = msg.message_id
        while message_id > main_message_id:
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

@router.callback_query(F.data == CallBacks.polls.value)
async def send_poll_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.polls.value)
    polls_list_mk = director_keyboards.polls_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=polls_list_mk)

@router.callback_query(F.data == CallBacks.add_poll.value)
async def add_poll_reply_handler(clbck: CallbackQuery):
    poll_id = add_poll(user_id=clbck.from_user.id)
    await clbck.message.edit_text(text=f'{get_poll_name(poll_id=poll_id)} id:{poll_id}')
    poll_list_mk = director_keyboards.poll_list_mk_generator(poll_id=poll_id)
    await clbck.message.edit_reply_markup(reply_markup=poll_list_mk)

@router.callback_query(F.data == CallBacks.presenters.value)
async def presenters_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.presenters.value)
    staff_list_mk = director_keyboards.staff_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=staff_list_mk)

# @router.callback_query(F.data == CallBacks.thread_1_prefix.value)
# async def thread_1_reply_handler(clbck: CallbackQuery):
#     poll_id = get_dialog_status(user_id=clbck.from_user.id).split(CallBacks.prefix_divider.value)[1]
#     set_poll_type(poll_id=poll_id, poll_type=Statuses.thread_1.value)
#     await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(clbck.from_user.id))
#     try:
#         await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=poll_id))
#     except:
#         pass
#     set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.none.value)

@router.callback_query(F.data == CallBacks.accept.value)
async def accepr_reply_handler (clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            dialog_prefix, dialog_data = get_dialog_status(user_id=clbck.from_user.id).split(CallBacks.prefix_divider.value)
            match dialog_prefix:
                case CallBacks.delete_poll_prefix.value:
                    delete_poll(poll_id=dialog_data)
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(clbck.from_user.id))
                    await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.polls_list_mk_generator())
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.none.value)

@router.callback_query(F.data == CallBacks.reject.value)
async def accept_reply_handler (clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(user_id=clbck.from_user.id)) 
            set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.none.value}')   

@router.callback_query(F.data == F.data)
async def custom_reply_handler(clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            clbck_prefix, clbck_data = clbck.data.split(CallBacks.prefix_divider.value)
            match clbck_prefix:
                
                case CallBacks.delete_stuff_prefix.value:
                    await clbck.message.answer(text=texts.delete_from_stuff_message_generator(username=clbck_data, role=Roles.delegate.value), reply_markup=common_keyboards.accept_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)
                
                case CallBacks.poll_id_prefix.value:
                    await clbck.message.edit_text(text=f'{MenuTexts.poll.value} id:{clbck_data}')
                    await clbck.message.edit_reply_markup(reply_markup=director_keyboards.poll_list_mk_generator(poll_id=clbck_data))
                
                case CallBacks.poll_name_prefix.value:
                    await clbck.message.answer(text=texts.WRITE_POLL_NAME, reply_markup=common_keyboards.back_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)
                
                case CallBacks.poll_type_prefix.value:
                    await clbck.message.answer(text=texts.SELECT_QUESTION_TYPE, reply_markup=director_keyboards.poll_types_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)
                
                case CallBacks.delete_poll_prefix.value:
                    await clbck.message.answer(text=texts.delete_from_polls_message_generator(poll_name=clbck_data), reply_markup=common_keyboards.accept_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)
                
                case CallBacks.add_question_prefix.value:
                    await clbck.message.answer(text=texts.ADD_QUESTION, reply_markup=common_keyboards.back_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)

                case CallBacks.thread_prefix.value:
                    poll_id = get_dialog_status(user_id=clbck.from_user.id).split(CallBacks.prefix_divider.value)[1]
                    match clbck_data:
                        case CallBacks.thread_1.value:
                            set_poll_type(poll_id=poll_id, poll_type=Statuses.thread_1.value)
                        case CallBacks.thread_2.value:
                            set_poll_type(poll_id=poll_id, poll_type=Statuses.thread_2.value)
                        case CallBacks.thread_3.value:
                            set_poll_type(poll_id=poll_id, poll_type=Statuses.thread_3.value)
                        case CallBacks.thread_junior.value:
                            set_poll_type(poll_id=poll_id, poll_type=Statuses.thread_junior.value)
                        case CallBacks.thread_global.value:
                            set_poll_type(poll_id=poll_id, poll_type=Statuses.thread_global.value)
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(clbck.from_user.id))
                    try:
                        await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=poll_id))
                    except:
                        pass
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.none.value)

@router.message()
async def message_handler(msg: Message):
    role = get_role(user_id=msg.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            dialog_prefix, dialog_data = get_dialog_status(user_id=msg.from_user.id).split(CallBacks.prefix_divider.value)
            match dialog_prefix:
                case CallBacks.add_question_prefix.value:
                    question = msg.text
                    await msg.answer(text=texts.SELECT_QUESTION_TYPE, reply_markup=common_keyboards.back_mk)
                case CallBacks.poll_name_prefix.value:
                    set_poll_name(poll_id=dialog_data, poll_name=msg.text)
                    await message_deleter(msg=msg, main_message_id=get_main_message_id(msg.from_user.id))
                    try:
                        await msg.bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=get_main_message_id(msg.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=dialog_data))
                    except:
                        pass
                    set_dialog_status(user_id=msg.from_user.id, dialog_status=DialogStatuses.none.value)
