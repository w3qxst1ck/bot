from aiogram import Router, types
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_message(message: types.Message) -> None:
    """Команда /start"""
    await message.answer("Hello message")