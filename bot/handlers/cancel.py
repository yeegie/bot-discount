from aiogram import Bot, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from helpers.keyboards.menu import menu
from database.schemas import UserSchema

from .routers import user_router

from random import choice


@user_router.callback_query(F.data == 'cancel')
async def cancel(callback_query: CallbackQuery, bot: Bot, state: FSMContext, user: UserSchema):
    phrases = ['Хорошо', 'Ок', '👌🏻', 'Отмена']
    
    if await state.get_state() is None:
        await bot.answer_callback_query(callback_query.id)
        await callback_query.message.answer('Не тыкай сюда, ты уже отменил')
        return
    
    await state.clear()
    await callback_query.message.answer(choice(phrases), reply_markup=menu(user.fixed_percent))
    await bot.answer_callback_query(callback_query.id)


@user_router.message(F.text.lower().startswith('отмена'))
@user_router.message(Command(commands='cancel'))
async def cancel_text(message: Message, bot: Bot, state: FSMContext, user: UserSchema):
    phrases = ['Хорошо', 'Ок', '👌🏻', 'Отмена']
    
    if await state.get_state() is None:
        return
    
    await state.clear()
    await message.answer(choice(phrases), reply_markup=menu(user.fixed_percent))
