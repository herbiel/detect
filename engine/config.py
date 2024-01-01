#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detect 
@File    ：config.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/12/31 18:18 
'''

BROKER_URL = 'redis://192.168.50.18:6379/0' # Broker配置，使用Redis作为消息中间件
CELERY_RESULT_BACKEND = 'redis://192.168.50.18:6379/1' # BACKEND配置，这里使用redis
CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间
CELERY_TIMEZONE='Asia/Shanghai'   # 时区配置
CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '2/20s'}}
CELERY_IMPORTS = (
    'engine.tasks',
   # 'engine.period_task'
)
