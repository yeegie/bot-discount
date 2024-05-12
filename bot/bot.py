from data import config
import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.enums.parse_mode import ParseMode

from aiohttp.web import Application, run_app
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from utils.executor import on_startup_notify, start_webhook, run_polling
from utils.requests_middleware import log_middleware

from handlers import routers

import time
from loguru import logger


logger.level('REQUEST', no=35, color="<blue>")


logger.add(config.LOG_REQUESTS_FILE, rotation='10 MB', compression='zip', level='REQUEST', format="{time} - {level} - {message}")
logger.add(config.LOG_OUT_FILE, rotation='10 MB', compression='zip', level='DEBUG')


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    logger.info(f'[⏳] Starting to launch the application...')
    time_start = time.time()

    dispatcher.include_router(router=routers.user_router)
    dispatcher.include_router(router=routers.admin_router)
    logger.info('[X] Routers included...')

    if not config.General.polling:
        await start_webhook(
            config.WebHook.complete_url,
            bot,
            config.WebHook.listen_address,
            config.WebHook.listen_port,
        )
        
    logger.info(f'[🤖] Bot started @{(await bot.get_me()).username} -- {(time.time() - time_start):.1f} sec.')

    if config.Telegram.on_startup_notify:
        await on_startup_notify(bot)


async def on_shutdown():
    logger.info('Stopping the bot...')
    await bot.delete_webhook()
    logger.info('[💀] Bot - Bye!')


if __name__ == '__main__':
    props = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
    bot = Bot(token=config.Telegram.token, default=props)

    storage = MemoryStorage()
    dispather = Dispatcher(storage=storage)
    dispather.startup.register(on_startup)
    dispather.shutdown.register(on_shutdown)

    if config.General.polling:
        asyncio.run(run_polling(bot, dispather))
    else:
        app = Application()

        # Requests logging
        if config.General.requests_log:
            app.middlewares.append(log_middleware)

        app['bot'] = bot
        app['dp'] = dispather

        SimpleRequestHandler(
            dispatcher=dispather,
            bot=bot
        ).register(app, config.WebHook.bot_path)

        setup_application(app, dispather, bot=bot)

        run_app(app, host=config.WebHook.listen_address, port=config.WebHook.listen_port)
