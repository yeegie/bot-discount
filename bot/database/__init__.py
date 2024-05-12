from tortoise import Tortoise
from data import config
from loguru import logger
import os


async def init_database():
    db_file_exist = config.DataBase.db_file in os.listdir(config.DataBase.db_path)

    if config.DataBase.type == 'sqlite' and db_file_exist is False:
        db_path = config.DataBase.db_path
        db_file = config.DataBase.db_file

        with open(db_path + db_file, 'a'):
            os.utime(db_path + db_file, None)
        logger.info(f'[!] Database created {db_path + db_file}')

    await Tortoise.init(
        db_url=config.DataBase.connection_string,
        modules={'models': ['database.models']}
    )

    await Tortoise.generate_schemas()
    logger.info(f'[X] Database({config.DataBase.type}) inited...')


async def close_database():
    await Tortoise.close_connections()
    logger.info('[X] Database closed...')
