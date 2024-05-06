from aiogram import Bot, Dispatcher
from loguru import logger
import asyncio

from .get_ipv4 import get_ipv4


async def on_startup_notify(bot: Bot):
    for user in [423420323]:
        await bot.send_message(
            chat_id=user, text=f'I\'m running.', disable_notification=True
        )
        logger.info(f'Notified superuser {user} about bot is started.')
        await asyncio.sleep(0.2)


async def start_webhook(url: str, bot: Bot, listen_address: str, listen_port: str):
    logger.info(f'[!] Server runned on http://{get_ipv4()}:{listen_port}')
    logger.info(f'[🌟] Webhook runned on {url}')
    await bot.set_webhook(url)


async def run_polling(bot: Bot, dp: Dispatcher):
    logger.warning('[!] Bot running on pooling mode')
    await dp.start_polling(bot)
