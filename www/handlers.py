import logging,functools
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def get(path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

@get('/')
def index(request):
    logging.info(request.method)
    # resp = web.Response(body=b'<h1>Index</h1>')
    # # 如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    # resp.content_type = 'text/html;charset=utf-8'
    # return resp
    text = '<h1>Index</h1>'
    return text

@get('/hello/{name}')
def hello(name,request):
    logging.info(request.method)
    text = '<h1>hello,%s</h1>' % name
    # resp = web.Response(body=text.encode('utf-8'))
    # # 如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    # resp.content_type = 'text/html;charset=utf-8'
    # return resp
    return text

