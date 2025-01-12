import asyncio
import logging

import src
import texts
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from handlers import router
from sqlite_db import connect_db


async def main():
    connect_db()

    bot = Bot(token=src.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.set_my_description(texts.BOT_DESCRIPRION)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())