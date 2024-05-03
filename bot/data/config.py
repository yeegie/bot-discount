from dotenv import load_dotenv
import os


load_dotenv()


class Telegram:
    '''
    ### Telegram settings storage
    Properties:
    * token - bot token from [@BotFather](https://t.me/BotFather)
    '''
    token = os.getenv('token')

    _all = [token]
    _fields = ['token']

    @classmethod
    def __str__(cls) -> str:
        return '=== Telegram ===\n' + '\n'.join(f"{field}: {getattr(cls, field)}" for field in cls._fields)


class WebHook:
    '''
    ### Webhook settings storage
    Properties:
    * listen_address
    * listen_port
    * base_url
    * bot_path
    * complete_url
    '''
    listen_address = os.getenv('listen_address')
    listen_port = int(os.getenv('listen_port'))
    base_url = os.getenv('base_url')
    bot_path = os.getenv('bot_path')
    complete_url = base_url + bot_path

    _all = [listen_address, listen_port, base_url, bot_path, complete_url]
    _fields = ['listen_address', 'listen_port', 'base_url', 'bot_path', 'complete_url']

    @classmethod
    def __str__(cls) -> str:
        return '=== WebHook ===\n' + '\n'.join(f"{field}: {getattr(cls, field)}" for field in cls._fields)
    

