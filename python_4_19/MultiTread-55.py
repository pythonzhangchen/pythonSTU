# -*- coding: utf-8 -*-
# @Time : 2022/4/19 16:28 
# @Author : chen.zhang 
# @File : MultiTread-55.py

# 关于 Queue队列

from queue import Queue
import threading

# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
#
# item = q.get()  # 从队列获取一个
# q.task_done()  # 类似一个list的 pop 取消元素，但是这里重点是 #任务完成# get也会减少队列数量元素数量
# item = q.get()
# q.task_done()
# item = q.get()
# q.task_done()
# # item = q.get() # 如果get为空 则等待
# # print(item)
# item = q.get()
# q.task_done()
# print(item)
#
# print(q.empty())

q = Queue(maxsize=0)


def product():
    while True:
        pro = input('产品：')
        q.put('生产{}'.format(pro), '\n')


def consume():
    while True:
        print('消费者购买{}:'.format(q.get()))


t1 = threading.Thread(target=product)
t2 = threading.Thread(target=consume)
t1.start()
t2.start()
t1.join()
t2.join()
print('main done')
