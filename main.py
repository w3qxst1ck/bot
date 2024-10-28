import asyncio
import os

import aiogram as io
import dotenv
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from router import router

load_dotenv()


async def start_bot() -> None:
    """Запуск бота"""
    bot = io.Bot(os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    storage = MemoryStorage()
    dispatcher = io.Dispatcher(storage=storage)

    dispatcher.include_routers(router)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())