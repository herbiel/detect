#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detect 
@File    ：app.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/12/31 18:15 
'''
import tornado
from tornado import websocket
from tornado import ioloop
from tornado import web
import logging
import audioop
import requests
import tornado.ioloop
import tornado.websocket
import tornado.httpserver
import tornado.template
import tornado.web
# import webrtcvad
from tornado.web import url
import os
import wave
import datetime
import whisper_at as whisper
import sys
import time


RATE = 8000


class MLModel(object):
    def __init__(self):
        self.model = whisper.load_model("tiny")
        logging.info(self.model)

    def predict_from_file(self, wav_file, verbose=False):
        result = self.model.transcribe(wav_file, at_time_res=10)
        audio_tag_result = whisper.parse_at_label(result, language='en', top_k=5, p_threshold=-1, include_class_list=list(range(527)))
        return audio_tag_result[0]['audio tags']

def save(id,audio):
    fn = "rec-{}.wav".format(id)
    output = wave.open(fn, 'wb')
    output.setparams(
        (1, 2, RATE, 0, 'NONE', 'not compressed'))
    output.writeframes(audio)
    return model.predict_from_file(fn)

class WSHandler(tornado.websocket.WebSocketHandler):
    def initialize(self):
        self.id = None
        self.ringtone_count = 0
        self.packet_count = 0
        self.detector_result_list = []
        self.payload = b''
        self.checkpayload = b''
        self.prediction_result = None
        self.last_execution_time = time.time()
        logging.info("client init")

    def open(self, path):
        logging.info("client connected")

    def on_message(self, message):

        asr_payload = b''
        # Check if message is Binary or Text
        if type(message) != str:
            self.packet_count = self.packet_count + 1
            self.payload += message



            ##test aliyun nls
            # self.asr_payload += self.now_asr_payload
            # self.voicecount = self.voicecount + 1
            # print  (self.count)
            # if len(self.now_asr_payload) > 0 and self.voicecount > 0:
            #    t = TestSt(self.id)
            #    print("start asr")
            #    self.result += t.test_run(self.now_asr_payload)
            #    self.now_asr_payload = b''
            #    self.voicecount = 0
            ##end test aliyun nls

            #    if self.vad.is_speech(frame, RATE):
            # print (self.vad.is_speech(frame, RATE))
            # try:
            #    data = sr.AudioData(frame, RATE, 2)
            #    result = r.recognize_google(data)
            #    print(result)
            # except Exception as e:
            #    print(e)
            #        self.payload += frame
            #        asr_payload += frame
            # print ("audio is %d"%len(asr_payload))
            # asr.test_run(frame)
            # if len(asr_payload) > 10000:
            #  t = TestSt()
            #  t.test_run(asr_payload)


        else:
            self.id = message
            logging.info(message)

    def on_close(self):
        # Remove the connection from the list of connections
        fn ="rec-{}.wav".format(self.id)
        output = wave.open(fn, 'wb')
        output.setparams(
            (1, 2, RATE, 0, 'NONE', 'not compressed'))
        output.writeframes(self.payload)


        # asr_task_record("record",self.id,"test",self.result)
        # print(speech_det(fn))
        # print(len(self.asr_payload))
        # prediction = model.predict_from_file(fn)
        # logging.info("prediction {}".format(prediction))
        logging.info(self.id)
        logging.info("client disconnected")


def main():
    try:
        global  model
        model = MLModel()
        logging.getLogger().setLevel(logging.INFO)
        application = tornado.web.Application([
            url(r"/(.*)", WSHandler),
        ])
        http_server = tornado.httpserver.HTTPServer(application)
        port = int(os.getenv('PORT', 8000))
        http_server.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass  # Suppress the stack-trace on quit


if __name__ == "__main__":
    main()
