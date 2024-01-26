import logging
from readline import replace_history_item
import aiogram
import texts
from aiogram import F, Router, exceptions
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from enums import CallBacks, DialogStatuses, MenuTexts, Roles, Statuses
from keyboards import common_keyboards, director_keyboards, delegate_keyboards
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
    add_question,
    set_question,
    delete_question,
    set_question_type,
    get_poll_id,
    get_question,
    get_poll_type,
    get_delegates
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
    except:
        message_deleter(msg, main_message_id)

@router.message(Command("conference"))
async def start_handler(msg: Message):
    set_main_message_id(user_id=msg.from_user.id, message_id=msg.message_id)
    await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
    role = add_user(user_id=msg.from_user.id, username=msg.from_user.username, mode=Statuses.conference_mode.value)
    match role:
        case Roles.delegate.value:
            await msg.answer(texts.GREETINGS_FOR_DELEGATE, reply_markup=common_keyboards.main_menu_mk)
        case Roles.director.value:
            await msg.answer(texts.GREETINGS_FOR_DIRECTOR, reply_markup=common_keyboards.main_menu_mk)
    set_dialog_status(user_id=msg.from_user.id, dialog_status=DialogStatuses.start.value)

@router.callback_query(F.data == CallBacks.main_menu.value)
async def main_menu_reply_handler(clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            await clbck.message.edit_text(text='Тут будут отображаться опросы')
        case Roles.director.value:
            await clbck.message.edit_text(text=MenuTexts.main_menu.value)
            await clbck.message.edit_reply_markup(reply_markup=director_keyboards.main_menu_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.main_menu.value)

@router.callback_query(F.data == CallBacks.polls.value)
async def send_poll_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.polls.value)
    polls_list_mk = director_keyboards.polls_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=polls_list_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.polls.value)

@router.callback_query(F.data == CallBacks.add_poll.value)
async def add_poll_reply_handler(clbck: CallbackQuery):
    poll_id = add_poll(user_id=clbck.from_user.id)
    await clbck.message.edit_text(text=f'{get_poll_name(poll_id=poll_id)} id:{poll_id}')
    poll_list_mk = director_keyboards.poll_list_mk_generator(poll_id=poll_id)
    await clbck.message.edit_reply_markup(reply_markup=poll_list_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{poll_id}')
    
@router.callback_query(F.data == CallBacks.poll_name.value)
async def poll_name_reply_handler(clbck: CallbackQuery):
    await clbck.message.answer(text=texts.WRITE_POLL_NAME, reply_markup=common_keyboards.back_mk)
    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll_name.value}{DialogStatuses.divider.value}{dialog_status}')

@router.callback_query(F.data == CallBacks.poll_type.value)
async def poll_type_reply_handler(clbck: CallbackQuery):
    await clbck.message.answer(text=texts.SELECT_QUESTION_TYPE, reply_markup=director_keyboards.poll_types_mk)
    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=dialog_status)

@router.callback_query(F.data == CallBacks.send_poll.value)
async def sed_poll_reply_handler(clbck: CallbackQuery):
    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
    object_name, object_id = dialog_status.split(DialogStatuses.divider.value)
    await clbck.message.answer(text=texts.SEND_POLL, reply_markup=common_keyboards.accept_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.send_poll.value}{DialogStatuses.divider.value}{dialog_status}')
    
@router.callback_query(F.data == CallBacks.add_question.value)
async def add_question_reply_handler(clbck: CallbackQuery):
    await clbck.message.answer(text=texts.ADD_QUESTION, reply_markup=common_keyboards.back_mk)
    question_id = add_question(poll_id=get_dialog_status(user_id=clbck.from_user.id).split(DialogStatuses.divider.value)[1])
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.set_question.value}{DialogStatuses.divider.value}{DialogStatuses.question.value}{DialogStatuses.divider.value}{question_id}')
    
@router.callback_query(F.data == CallBacks.change_question.value)
async def change_question_reply_handler(clbck: CallbackQuery):
    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
    object_name, object_id = dialog_status.split(DialogStatuses.divider.value)
    await clbck.message.answer(text=texts.ADD_QUESTION, reply_markup=common_keyboards.back_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.change_question.value}{DialogStatuses.divider.value}{DialogStatuses.question.value}{DialogStatuses.divider.value}{object_id}')    

@router.callback_query(F.data == CallBacks.change_question_type.value)
async def change_question_type_reply_handler(clbck: CallbackQuery):
    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
    object_name, object_id = dialog_status.split(DialogStatuses.divider.value)
    await clbck.message.answer(text=texts.SELECT_QUESTION_TYPE, reply_markup=director_keyboards.question_types_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.change_question_type.value}{DialogStatuses.divider.value}{object_name}{DialogStatuses.divider.value}{object_id}')
    
@router.callback_query(F.data == CallBacks.delete.value)
async def delete_reply_handler(clbck: CallbackQuery):
    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
    object_name, object_id = dialog_status.split(DialogStatuses.divider.value)
    match object_name:
        case DialogStatuses.poll.value:
            await clbck.message.answer(text=texts.delete_from_polls_message_generator(poll_name=get_poll_name(poll_id=object_id)), reply_markup=common_keyboards.accept_mk)
            set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.delete.value}{DialogStatuses.divider.value}{dialog_status}')
        case DialogStatuses.question.value:
            await clbck.message.answer(text=texts.DELETE_QUESTION, reply_markup=common_keyboards.accept_mk)
            set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.delete.value}{DialogStatuses.divider.value}{dialog_status}')
            
@router.callback_query(F.data == CallBacks.presenters.value)
async def presenters_reply_handler(clbck: CallbackQuery):
    await clbck.message.edit_text(text=MenuTexts.presenters.value)
    staff_list_mk = director_keyboards.staff_list_mk_generator()
    await clbck.message.edit_reply_markup(reply_markup=staff_list_mk)
    set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.presenters.value)


@router.callback_query(F.data == CallBacks.accept.value)
async def accepr_reply_handler (clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            dialog_prefix, object_name, object_id = get_dialog_status(user_id=clbck.from_user.id).split(DialogStatuses.divider.value)
            match dialog_prefix:
                case DialogStatuses.delete.value:
                    match object_name: 
                        case DialogStatuses.poll.value:
                            delete_poll(poll_id=object_id)
                            await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(clbck.from_user.id))
                            await clbck.bot.edit_message_text(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), text=MenuTexts.polls.value)
                            await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.polls_list_mk_generator())
                            set_dialog_status(user_id=clbck.from_user.id, dialog_status=DialogStatuses.polls.value)
                        case DialogStatuses.question.value:
                            poll_id = delete_question(question_id=object_id)
                            await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(user_id=clbck.from_user.id)) 
                            await clbck.bot.edit_message_text(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), text=f'{get_poll_name(poll_id=poll_id)} id:{poll_id}')
                            await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=poll_id))
                            set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{poll_id}') 
                case DialogStatuses.send_poll.value:
                    poll_type = get_poll_type(poll_id=object_id)
                    delegate_ids = get_delegates(thread=poll_type)
                    for id in delegate_ids:
                        await clbck.bot.send_message(chat_id=id[0], text=get_poll_name(poll_id=object_id), reply_markup=delegate_keyboards.answer_mk_generator(object_id))
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(user_id=clbck.from_user.id)) 
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{object_id}')
                    
                    
@router.callback_query(F.data == CallBacks.reject.value)
async def accept_reply_handler (clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    match role:
        case Roles.delegate.value:
            object_name, object_id = get_dialog_status(user_id=clbck.from_user.id).split(DialogStatuses.divider.value)
            # await clbck.message.edit_text(text=)
            # await clbck.message.edit_reply_markup(reply_markup=)
        case Roles.director.value:
            dialog_prefix, object_name, object_id = get_dialog_status(user_id=clbck.from_user.id).split(DialogStatuses.divider.value)
            match dialog_prefix:
                case DialogStatuses.set_question.value | DialogStatuses.set_question_type.value:
                    poll_id = delete_question(question_id=object_id)
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(user_id=clbck.from_user.id)) 
                    await clbck.bot.edit_message_text(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), text=f'{get_poll_name(poll_id=poll_id)} id:{poll_id}')
                    await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=poll_id))
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{poll_id}') 
                case DialogStatuses.change_question_type.value | DialogStatuses.change_question.value:
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(user_id=clbck.from_user.id)) 
                    await clbck.bot.edit_message_text(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), text=get_question(question_id=object_id))
                    await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.question_list_mk_generator(question_id=object_id))
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.question.value}{DialogStatuses.divider.value}{object_id}') 
                case DialogStatuses.send_poll.value:
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(user_id=clbck.from_user.id)) 
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{object_id}') 
                    
@router.callback_query(F.data == F.data)
async def custom_reply_handler(clbck: CallbackQuery):
    role = get_role(user_id=clbck.from_user.id)
    object_name, object_id = clbck.data.split(CallBacks.prefix_divider.value)
    match role:
        case Roles.delegate.value:
            match object_name:
                case CallBacks.answer.value:
                    await clbck.message.edit_text(text=get_poll_name(poll_id=object_id))
                    await clbck.message.edit_reply_markup(reply_markup=delegate_keyboards.poll_list_mk_generator(poll_id=object_id))
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{object_id}')
                    
        case Roles.director.value:
            match object_name:
                
                case CallBacks.delete_stuff_prefix.value:
                    await clbck.message.answer(text=texts.delete_from_stuff_message_generator(username=object_id, role=Roles.delegate.value), reply_markup=common_keyboards.accept_mk)
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)
                
                case DialogStatuses.poll.value:
                    await clbck.message.edit_text(text=f'{get_poll_name(poll_id=object_id)} id:{object_id}')
                    await clbck.message.edit_reply_markup(reply_markup=director_keyboards.poll_list_mk_generator(poll_id=object_id))
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=clbck.data)
                    
                case CallBacks.thread_prefix.value:
                    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
                    poll_id = dialog_status.split(DialogStatuses.divider.value)[1]
                    match object_id:
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
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=dialog_status)
                    
                case CallBacks.question.value:
                    await clbck.message.edit_text(text=get_question(question_id=object_id))
                    await clbck.message.edit_reply_markup(reply_markup=director_keyboards.question_list_mk_generator(question_id=object_id))
                    set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{object_name}{DialogStatuses.divider.value}{object_id}')

                case CallBacks.set_question_type.value:
                    dialog_status = get_dialog_status(user_id=clbck.from_user.id)
                    dialog_prefix = dialog_status.split(DialogStatuses.divider.value)[0]
                    question_id = dialog_status.split(DialogStatuses.divider.value)[2]
                    poll_id = get_poll_id(question_id=question_id)
                    match object_id:
                        case CallBacks.question_type_text.value:
                            set_question_type(question_id=question_id, question_type=Statuses.type_text.value)
                        case CallBacks.question_type_1_5.value:
                            set_question_type(question_id=question_id, question_type=Statuses.type_1_5.value)
                        case CallBacks.question_type_1_10.value:
                            set_question_type(question_id=question_id, question_type=Statuses.type_1_10.value)
                    await message_deleter(msg=clbck.message, main_message_id=get_main_message_id(clbck.from_user.id))
                    match dialog_prefix:
                        case DialogStatuses.set_question_type.value:
                            set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.poll.value}{DialogStatuses.divider.value}{poll_id}')
                            await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=poll_id))
                        case DialogStatuses.change_question_type.value:
                            set_dialog_status(user_id=clbck.from_user.id, dialog_status=f'{DialogStatuses.question.value}{DialogStatuses.divider.value}{question_id}')
                            await clbck.bot.edit_message_reply_markup(chat_id=clbck.message.chat.id, message_id=get_main_message_id(clbck.from_user.id), reply_markup=director_keyboards.question_list_mk_generator(question_id=question_id))
                case _:
                    logging.warning(f'Empty handler callback:{clbck.data}')
                            

@router.message()
async def message_handler(msg: Message):
    role = get_role(user_id=msg.from_user.id)
    match role:
        case Roles.delegate.value:
            pass
        case Roles.director.value:
            dialog_prefix, object_name, object_id = get_dialog_status(user_id=msg.from_user.id).split(CallBacks.prefix_divider.value)
            match dialog_prefix:
                case CallBacks.set_question_prefix.value:
                    set_question(question_id=object_id, question=msg.text)
                    await msg.answer(text=texts.SELECT_QUESTION_TYPE, reply_markup=director_keyboards.question_types_mk)
                    set_dialog_status(user_id=msg.from_user.id, dialog_status=f'{DialogStatuses.set_question_type.value}{DialogStatuses.divider.value}{object_name}{DialogStatuses.divider.value}{object_id}')
                
                case DialogStatuses.change_question.value:
                    set_question(question_id=object_id, question=msg.text)
                    await message_deleter(msg=msg, main_message_id=get_main_message_id(user_id=msg.from_user.id)) 
                    await msg.bot.edit_message_text(chat_id=msg.chat.id, message_id=get_main_message_id(msg.from_user.id), text=get_question(question_id=object_id))
                    await msg.bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=get_main_message_id(msg.from_user.id), reply_markup=director_keyboards.question_list_mk_generator(question_id=object_id))
                    set_dialog_status(user_id=msg.from_user.id, dialog_status=f'{DialogStatuses.question.value}{DialogStatuses.divider.value}{object_id}')
                
                case DialogStatuses.poll_name.value:
                    set_poll_name(poll_id=object_id, poll_name=msg.text)
                    await message_deleter(msg=msg, main_message_id=get_main_message_id(msg.from_user.id))
                    try:
                        await msg.bot.edit_message_text(chat_id=msg.chat.id, message_id=get_main_message_id(msg.from_user.id), text=f'{get_poll_name(poll_id=object_id)} id:{object_id}')
                        await msg.bot.edit_message_reply_markup(chat_id=msg.chat.id, message_id=get_main_message_id(msg.from_user.id), reply_markup=director_keyboards.poll_list_mk_generator(poll_id=object_id))
                    except:
                        pass
                    set_dialog_status(user_id=msg.from_user.id, dialog_status=f'{object_name}{DialogStatuses.divider.value}{object_id}')
