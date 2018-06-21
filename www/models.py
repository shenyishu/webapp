#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import aiomysql
import time, uuid
import asyncio, logging
from www.orm import Model, StringField, BooleanField, FloatField, TextField, create_pool

# logging.basicConfig(level=logging.INFO)

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

if __name__ == "__main__":  # 一个类自带前后都有双下划线的方法，在子类继承该类的时候，这些方法会自动调用，比如__init__

    loop = asyncio.get_event_loop()


    # 创建实例
    @asyncio.coroutine
    def test():
        yield from create_pool(loop=loop, host='localhost', port=3306, user='root', password='shen1987', db='awesome')
        u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

        yield from u.save()


    loop.run_until_complete(test())
    loop.run_forever()
    # if loop.is_closed():
    #     sys.exit(0)