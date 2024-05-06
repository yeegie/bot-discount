from aiohttp.web import Application, Request, Response
from loguru import logger

async def log_middleware(app: Application, handler: callable) -> callable:
    async def middleware_handler(request: Request):
        logger.log('REQUEST', f'Request: {request.method} {request.path}')
        response: Response = await handler(request)
        logger.log('REQUEST', f'Response: {response.status}')
        return response
    return middleware_handler
