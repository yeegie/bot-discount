from data.config import Telegram, WebHook

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.enums.parse_mode import ParseMode

from aiohttp.web import Application, run_app, post
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from handlers import routers

import time
from loguru import logger


LOG_OUT_FILE = 'logs/bot.log'
logger.add(LOG_OUT_FILE, rotation='10 MB', compression='zip', level='DEBUG')


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    logger.info(f'[⏳] Starting to launch the application...')
    time_start = time.time()

    dispatcher.include_router(router=routers.user_router)
    dispatcher.include_router(router=routers.admin_router)
    logger.info('[X] Routers included...')

    await bot.set_webhook(f"{WebHook.base_url}{WebHook.bot_path}")
    logger.info(f'[🤖] Bot started @{(await bot.get_me()).username} -- {(time.time() - time_start):.1f} sec.')
    # logger.info(f'[🌟] App runned on http://{WebHook.listen_address}:{WebHook.listen_port}/ @@ {WebHook.base_url}{WebHook.bot_path}')


async def on_shutdown():
    logger.info('Stopping the bot...')
    await bot.delete_webhook()
    logger.info('[💀] Bot - Bye!')


if __name__ == '__main__':
    props = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )

    bot = Bot(token=Telegram.token, default=props)

    storage = MemoryStorage()
    dispather = Dispatcher(storage=storage)
    dispather.startup.register(on_startup)
    dispather.shutdown.register(on_shutdown)

    app = Application()

    app['bot'] = bot
    app['dp'] = dispather

    SimpleRequestHandler(dispatcher=dispather, bot=bot).register(app, WebHook.bot_path)

    setup_application(app, dispather, bot=bot)
    run_app(app, host=WebHook.listen_address, port=WebHook.listen_port)
