# -*- coding: utf-8 -*-
# @Time : 2022/4/19 16:09 
# @Author : chen.zhang 
# @File : MultiTread-44.py
import threading
import os, time

# 线程锁

# my_balance = 1000  # 余额
#
#
# def C1(payment):
#     global my_balance
#     if my_balance >= payment:
#         time.sleep(0.1)
#         my_balance = my_balance - payment
#
#
# def C2(payment):
#     global my_balance
#     if my_balance >= payment:
#         time.sleep(0.1)
#         my_balance = my_balance - payment
#
#
# T = []
# consume1 = threading.Thread(target=C1, args=(800,))
# consume2 = threading.Thread(target=C2, args=(600,))
#
# T.append(consume1)
# T.append(consume2)
#
# for s in T:
#     s.start()
#
# for j in T:
#     j.join()
#
# print(my_balance)
# print('python主线程结束')

my_balance = 1000  # 余额


def C1(payment, who, L):
    global my_balance
    L.acquire()
    if my_balance >= payment:
        time.sleep(0.1)
        my_balance = my_balance - payment
    else:
        print(who)
        print('余额不足')
    L.release()


def C2(payment, who, L):
    global my_balance
    L.acquire()
    if my_balance >= payment:
        time.sleep(0.1)
        my_balance = my_balance - payment
    else:
        print(who)
        print('余额不足')
    L.release()


L = threading.Lock()
T = []
consume1 = threading.Thread(target=C1, args=(800, '媳妇', L))
consume2 = threading.Thread(target=C2, args=(600, '老公', L))

T.append(consume1)
T.append(consume2)

for s in T:
    s.start()

for j in T:
    j.join()

print(my_balance)
print('python主线程结束')
