from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton
from ..fabrics.error import ErrorCallback


def error(title: str = 'Исправить 😧', state: str = ''):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=title, callback_data=ErrorCallback(action='change', state_to=state).pack()))

    return builder.as_markup(resize_keyboard=True)
