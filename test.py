#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detect 
@File    ：test.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/12/31 18:24 
'''
from engine.tasks import add_numbers

print(add_numbers.delay(2,9))