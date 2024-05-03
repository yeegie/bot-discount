from aiogram import Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from aiogram.fsm.context import FSMContext
from helpers.states import states

from helpers.keyboards.cancel import cancel_inline, cancel_reply
from helpers.keyboards.error import error
from helpers.keyboards.menu import menu

from helpers.fabrics.error import ErrorCallback

from ..routers import user_router

from loguru import logger


@user_router.message(Command(commands=['percent']))
@user_router.message(F.text.lower().startswith('процент'))
async def calculate_start(message: Message, state: FSMContext):
    await state.set_state(states.CalculatePricePercent.percent)
    await message.answer('🪙')
    await message.answer('Введи процент, в следующем формате\n└ <code>15%</code> / <code>15</code>', reply_markup=cancel_inline('Я передумал 🙅🏻‍♂️'))


@user_router.message(states.CalculatePricePercent.percent)
async def calculate_percent(message: Message, state: FSMContext):
    percent = float(message.text.replace('%', ''))
    if percent > 100:
        await message.answer('Введи не больше 100')
        return

    await message.answer(f'Твой процент: {percent}%', reply_markup=error(state='percent'))
    await message.answer(f'Теперь введи число', reply_markup=cancel_reply())

    await state.update_data(percent=percent / 100)
    await state.set_state(states.CalculatePricePercent.value)


@user_router.message(states.CalculatePricePercent.value)
async def calculate_value(message: Message, state: FSMContext):
    try:
        value = float(message.text)
        percent = (await state.get_data())['percent']
    except ValueError:
        await message.answer('Введи число', reply_markup=cancel_inline())

    await message.answer(f'<code>{round(value - (value * percent), 2)}</code> ₽', reply_markup=menu())
    await state.clear()


@user_router.callback_query(ErrorCallback.filter(F.action == 'change'))
async def error_handler(callback_query: CallbackQuery, callback_data: ErrorCallback, bot: Bot, state: FSMContext):
    avaiable_states = {
        'percent': states.CalculatePricePercent.percent,
        'value': states.CalculatePricePercent.value,
    }

    await state.set_state(avaiable_states[callback_data.state_to])
    await callback_query.message.answer('Введи новое значение')
    await bot.answer_callback_query(callback_query.id)
