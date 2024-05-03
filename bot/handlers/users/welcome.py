from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from helpers.keyboards.menu import menu

from ..routers import user_router


@user_router.message(Command(commands=['start']))
async def welcome(message: Message, bot: Message, state: FSMContext):
    await state.clear()
    await message.answer('🤖')
    await message.answer(f'Привет, @{message.from_user.username}!', reply_markup=menu())
