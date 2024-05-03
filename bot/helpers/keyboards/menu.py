from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton


def menu():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Число'), KeyboardButton(text='Процент'))

    return builder.as_markup(resize_keyboard=True)
