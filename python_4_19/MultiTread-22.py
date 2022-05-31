# -*- coding: utf-8 -*-
# @Time : 2022/4/19 15:53 
# @Author : chen.zhang 
# @File : MultiTread-22.py
import threading
import os, time


# 线程阻塞（加入主线程） join 让子线程执行完成才能继续执行主线程

def my_task1(name, message, a, b):
    print('i am %s' % name)
    time.sleep(1)
    print(message)


def my_task2(name, message):
    print('i am %s' % name)
    time.sleep(1.5)
    print(message)


T1 = threading.Thread(name='T1', target=my_task1, args=('正正', 'Hello World'), kwargs=({'a': 1, 'b': 2}))
T2 = threading.Thread(name='T2', target=my_task2, args=('培培', 'Hello Python'))

T1.start()
T2.start()

T1.join()
T2.join()
print('Python主线程结束')
