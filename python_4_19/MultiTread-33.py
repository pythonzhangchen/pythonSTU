# -*- coding: utf-8 -*-
# @Time : 2022/4/19 16:01 
# @Author : chen.zhang 
# @File : MultiTread-33.py

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


def my_task3(name, message):
    print('i am %s' % name)
    time.sleep(10)
    print(message)


T1 = threading.Thread(target=my_task1, args=('正正', 'Hello World'))
T2 = threading.Thread(target=my_task2, args=('培培', 'Hello Python'))
T3 = threading.Thread(target=my_task3, args=('宁夫', 'Hello Django'))

T3.setDaemon(True)

T1.start()
T2.start()
T3.start()

print(threading.activeCount())

print('Python主线程结束')