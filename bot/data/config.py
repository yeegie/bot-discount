from envparse import env

env.read_envfile('.env')


LOG_OUT_FILE = 'logs/bot.log'
LOG_REQUESTS_FILE = 'logs/requests.log'


class Telegram:
    '''
    ### Telegram settings storage
    Properties:
    * token - bot token from [@BotFather](https://t.me/BotFather)
    * on_startup_notify - startup notification for admins. default False.
    '''
    token = env.str('token')
    on_startup_notify = env.bool('on_startup_notify', default=False)

    _all = [token]
    _fields = ['token', 'on_startup_notify']

    @classmethod
    def __str__(cls) -> str:
        return '=== Telegram ===\n' + '\n'.join(f"{field}: {getattr(cls, field)}" for field in cls._fields)
    

class General:
    '''
    ### General settings storage
    Properties:
    * polling - startup type, accepts: true | false
    '''
    polling = env.bool('polling', default=False)

    _all = [polling]
    _fields = ['polling']

    @classmethod
    def __str__(cls) -> str:
        return '=== General ===\n' + '\n'.join(f"{field}: {getattr(cls, field)}" for field in cls._fields)


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
    listen_address = env.str('listen_address')
    listen_port = env.int('listen_port')
    base_url = env.str('base_url')
    bot_path = env.str('bot_path')
    complete_url = base_url + bot_path

    _all = [listen_address, listen_port, base_url, bot_path, complete_url]
    _fields = ['listen_address', 'listen_port', 'base_url', 'bot_path', 'complete_url']

    @classmethod
    def __str__(cls) -> str:
        return '=== WebHook ===\n' + '\n'.join(f"{field}: {getattr(cls, field)}" for field in cls._fields)
    

