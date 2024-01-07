import texts
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from enums import CallBacks, DialogStatuses
# from keyboards import 
from sqlite_db import add_user
# from validators import

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    role = add_user(user_id=msg.from_user.id, username=msg.from_user.username, role=1)
    