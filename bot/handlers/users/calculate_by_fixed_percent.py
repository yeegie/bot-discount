from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command

from aiogram.fsm.context import FSMContext
from helpers.states import states
from helpers.keyboards.cancel import cancel_inline
from helpers.functions.calculate import calculate_number

from database.schemas import UserSchema

from ..routers import user_router

from loguru import logger


@user_router.message(Command(commands=['fixed']))
@user_router.message(F.text[-1] == '%')
async def calculate_start(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(states.CalculateFixedPercent.value)
    await message.answer('💸')
    await message.answer('Введи число', reply_markup=cancel_inline('Я передумал 🙅🏻‍♂️'))


@user_router.message(states.CalculateFixedPercent.value)
async def get_value(message: Message, state: FSMContext, user: UserSchema):
    try:
        value = float(message.text)
    except ValueError:
        await message.answer('Введи число', reply_markup=cancel_inline())

    await message.answer(f'<code>{round(value - (value * (user.fixed_percent / 100)), 2)}</code> ₽')
    await state.clear()
