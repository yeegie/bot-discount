from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton


def cancel_inline(title: str = 'Отмена ❌'):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=title, callback_data='cancel'))

    return builder.as_markup(resize_keyboard=True)


def cancel_reply(title: str = 'Отмена ❌'):
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text=title))

    return builder.as_markup(resize_keyboard=True)
