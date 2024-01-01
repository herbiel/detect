#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detect 
@File    ：tasks.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/12/31 18:19 
'''

import celery
import time
from celery.utils.log import get_task_logger
from engine import app
import whisper_at as whisper
import sys

model = whisper.load_model("tiny")
@app.task
def add_numbers(x, y):
    result = x + y
    return result

@app.task
def detect(file):
    model = whisper.load_model("tiny")
    result = model.transcribe(file, at_time_res=10)
    audio_tag_result = whisper.parse_at_label(result, language='en', top_k=5, p_threshold=-1,include_class_list=list(range(527)))
    try:
        tag = audio_tag_result[0]['audio tags']
        asr_text = result["text"]
        ##save to db
    except Exception as e:
        ##save error result to db
        pass
