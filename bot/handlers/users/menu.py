from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command

from helpers.keyboards.menu import menu
from database.schemas import UserSchema

from ..routers import user_router


@user_router.message(Command(commands='menu'))
@user_router.message(F.text.lower().startswith('меню 🕹'))
async def show_menu(message: Message, user: UserSchema):
    await message.answer('🕹', reply_markup=menu(user.fixed_percent))