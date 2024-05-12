from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton
from typing import Optional


def menu(fixed_percent: Optional[float] = None):
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Число'), KeyboardButton(text='Процент'))

    if fixed_percent is not None:
        builder.row(KeyboardButton(text=f'{fixed_percent} %'))

    builder.row(KeyboardButton(text='Настройки 🛠'))

    return builder.as_markup(resize_keyboard=True)
