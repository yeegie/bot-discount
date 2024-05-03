from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command

from aiogram.fsm.context import FSMContext
from helpers.states import states
from helpers.keyboards.cancel import cancel_inline
from helpers.functions.calculate import calculate_number

from ..routers import user_router

from loguru import logger


@user_router.message(Command(commands=['number']))
@user_router.message(F.text.lower().startswith('число'))
async def calculate_start(message: Message, state: FSMContext):
    await state.set_state(states.CalculatePriceNumber.value)
    await message.answer('💰')
    await message.answer('Введи цену, я рассчитаю скидки', reply_markup=cancel_inline('Я передумал 🙅🏻‍♂️'))


@user_router.message(states.CalculatePriceNumber.value)
async def calculate_value(message: Message, state: FSMContext):
    try:
        value = float(message.text)
    except ValueError:
        await message.answer('Введи число', reply_markup=cancel_inline())

    await message.answer(calculate_number(value))
    await state.clear()
