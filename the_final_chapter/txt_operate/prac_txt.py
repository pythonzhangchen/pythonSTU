# -*- coding: utf-8 -*-
# @Time : 2022/4/27 16:41 
# @Author : chen.zhang 
# @File : prac_txt.py
import datetime
import os
import pickle
import random
import time

my_data = ['Sophia',
           'Emma',
           'Ava',
           'Mia',
           'Isabella',
           'Zoe',
           'Lily',
           'Emily',
           'Madison',
           'Jackson',
           'Lucas',
           'Mason',
           'Ethan',
           'Logan',
           'Jacob',
           'Olivia', ]


# 简单说下枚举
# for i, data in enumerate(my_data):
#     print(i, data)


def writeTEST():
    with open('txts/test.txt', 'a+') as w:  # a 是 add的意思
        for i, data in enumerate(my_data[0:5]):
            time.sleep(random.uniform(0, 1))  # 0 到1 之间的实数，包含了float
            w.write(str(i) + ' ' + str(data) + ' ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n')
        # 保存 当前总行数 为后边的计数做好准备


# writeTEST()


def writetxt():
    # 非第一次写入
    if os.path.exists('plk_she/counter.plk'):
        # 读取持久化对象 里的排位
        with open('plk_she/counter.plk', 'rb') as r:
            counter = pickle.load(r)
            print(counter)
        # 写入数据 注意这里取了0到5的数据
        with open('txts/1.txt', 'a') as w:
            for i, data in enumerate(my_data[0:5]):
                time.sleep(random.uniform(0, 1))
                w.write(
                    str(i + counter) + ' ' + str(data) + ' ' + str(
                        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n')
        # 保存 当前总行数，为以后的计数做好准备
        with open('plk_she/counter.plk', 'wb') as w:
            with open('txts/1.txt', 'r') as r:
                counter = len(r.readlines())
                pickle.dump(counter, w)
    # 第一次写入
    else:
        # 第一次写入要先写入
        with open('txts/1.txt', 'a') as w:
            for i, data in enumerate(my_data[0:5]):
                time.sleep(random.uniform(0, 1))
                w.write(
                    str(i) + ' ' + str(data) + ' ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n')
        # 写入 后进行计数
        with open('plk_she/counter.plk', 'wb') as w:
            counter = len(my_data[0:5])
            pickle.dump(counter, w)


# writetxt()

def readtxt():
    with open('txts/1.txt', 'r') as r:
        # print(r.readlines())
        for x in r.readlines():
            # print(x)
            print(x.strip().split(' '))  # strip干掉空行


# readtxt()


### 插入操作 ###
def insert_data(pos, name):
    new = []
    with open('txts/1.txt', 'r+') as r:
        for data in r.readlines():
            print(data.strip())
            new.append(' '.join(data.strip().split(' ')[1:4]))
    print(new)
    new.insert(pos, name + ' ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    with open('txts/1.txt', 'w+') as w:
        for x, data in enumerate(new):
            w.write(str(x) + ' ' + str(data) + '\n')
    print(new)

insert_data(1,'zzzz')