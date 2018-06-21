import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from www.coroweb import add_routes

logging.basicConfig(level=logging.INFO)

async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # await asyncio.sleep(0.3)
        return (await handler(request))
    return logger

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r = yield from handler(request)
        # if isinstance(r, dict):
        #     template = r.get('__template__')
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/html;charset=utf-8'
        return resp
    return response

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop,middlewares=[logger_factory,response_factory])
    add_routes(app, 'www.handlers')
    srv = yield from loop.create_server(app.make_handler(), 'localhost', 8080)
    logging.info('server started at http://localhost:8080...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()