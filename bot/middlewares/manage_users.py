from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, CallbackQuery

from database.models import User


class ManageUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user = await User.get_or_none(user_id=event.from_user.id)

        is_bot = False
        if isinstance(event, Message):
            is_bot = event.from_user.is_bot
        elif isinstance(event, CallbackQuery):
            is_bot = event.message.from_user.is_bot

        if not is_bot:
            bot: Bot = data['bot']
            if user is None:
                user = await User.create(
                    user_id=event.from_user.id,
                    full_name=event.from_user.full_name,
                    username=event.from_user.username,
                    language=event.from_user.language_code,
                )
            else:
                if user.full_name != event.from_user.username or user.username != event.from_user.username:
                    user.full_name = event.from_user.full_name
                    user.username = event.from_user.username
                    await user.save()
        
        data['user'] = user
        return await handler(event, data)
    