from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from database.schemas import UserSchema

from helpers.keyboards.settings import settings

from ...routers import user_router


@user_router.message(Command('settings'))
@user_router.message(F.text.lower().startswith('настройки'))
async def welcome(message: Message, bot: Message, state: FSMContext, user: UserSchema):
    await message.answer('🧰')
    await message.answer('Настройки', reply_markup=settings(user.fixed_percent))
