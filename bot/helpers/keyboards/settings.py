from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton
from typing import Optional


def settings(fixed_percent: Optional[float] = None):
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text=f'Изменить фиксированный процент {fixed_percent} %'))

    builder.row(KeyboardButton(text='Меню 🕹'))

    return builder.as_markup(resize_keyboard=True)
