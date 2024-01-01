#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detect 
@File    ：__init__.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/12/31 18:20 
'''
from celery import Celery
app = Celery('engine')  # 创建 Celery 实例
app.config_from_object('engine.config')
