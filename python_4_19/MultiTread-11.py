# -*- coding: utf-8 -*-
# @Time : 2022/4/19 15:47 
# @Author : chen.zhang 
# @File : MultiTread-11.py
import threading
import os, time


def my_task1(name, message):
    print('i am %s' % name)
    time.sleep(1)
    print(message)


def my_task2(name, message):
    print('i am %s' % name)
    time.sleep(1.5)
    print(message)


T1 = threading.Thread(target=my_task1, kwargs=({"name": '正正', "message": 'Hello World'}))
T2 = threading.Thread(target=my_task2, args=('培培', 'Hello Python'))
T1.start()
T2.start()

print('python主线程结束')
