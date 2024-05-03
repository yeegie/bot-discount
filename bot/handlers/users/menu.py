from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command

from helpers.keyboards.menu import menu

from ..routers import user_router


@user_router.message(Command(commands='menu'))
async def show_menu(message: Message):
    await message.answer('Используй кнопки ниже для навигации 🕹', reply_markup=menu())