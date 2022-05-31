# -*- coding: utf-8 -*-
# @Time : 2022/4/6 16:45 
# @Author : chen.zhang 
# @File : python_4_6.py
import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        return end - start

    return wrapper


@timer
def consumer1():
    i_data = []
    for x in range(10000000):
        i_data.append(x)


print(consumer1())
