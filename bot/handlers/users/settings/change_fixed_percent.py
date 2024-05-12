from aiogram import Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from helpers.keyboards.settings import settings
from helpers.keyboards.cancel import cancel_inline
from helpers.states import states

from database.models.user import User

from ...routers import user_router


@user_router.message(F.text.lower().startswith('изменить фиксированный процент'))
async def change_fixed_percent_start(message: Message, state: FSMContext):
    await state.set_state(states.ChangePercent.percent)
    await message.answer('Введи число, например: <code>25.5</code>', reply_markup=cancel_inline())


@user_router.message(states.ChangePercent.percent)
async def get_percent(message: Message, state: FSMContext):
    try:
        new_percent = float(message.text)
        if new_percent > 100:
            raise ValueError('percent > 100')
    except ValueError:
        await message.answer('Введи число', reply_markup=cancel_inline())

    user = await User.get(user_id=message.from_user.id)
    user.fixed_percent = new_percent
    await user.save()
    await message.answer('Изменил 🤏🏻', reply_markup=settings(user.fixed_percent))
    await state.clear()
