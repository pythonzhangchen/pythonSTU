# -*- coding: utf-8 -*-
# @Time : 2022/4/19 17:08 
# @Author : chen.zhang 
# @File : MultiTread-66.py

# 关于 Queue 队列和threading 线程的综合使用
# 这个应用很有意义
# **我是一个购物狂** 设计一个程序 一口气可以从商店买3个物品 连续购买6次

import threading, time
from queue import Queue


# 定义每个买手的功能
def buyer(q, L):
    current_t = threading.current_thread()  # 查看当前线程号
    while True:
        my_buy = q.get()

        with L:  # 注意lock这里的用途 使用上下文管理器 L.acquire() L.release()
            time.sleep(0.5)
            print(current_t, '--------', my_buy, sep='\n')
        q.task_done()


q = Queue(maxsize=0)  # 实例化一个队列 （定一个购买物品清单） # 特别注意队列是在主线程上
L = threading.Lock()

# 看看商店里都有啥
products = ['袜子', '电脑', '水杯', '洗衣机', '电视', '手机', '笔记本', '风扇', '空调', '航模', '眼睛', '毛巾', '充电宝', '微波炉', '茶杯', '茶叶', '投影',
            '桌子', '香水', '洗发水', '电冰箱', '摩托车', '汽车', 'Tshirt']

# 向队列添加 商品
for product in products:
    q.put(product)

# 准备多线程
number_buyers = 3
for t in range(number_buyers):
    buyer_t = threading.Thread(target=buyer, args=(q, L))
    buyer_t.setDaemon(True)   # 特别注意这里 为什么要这么设计？ 因为一旦队列没有东西了就会等待新的东西，那么需要守护线程来结束这个线程
    buyer_t.start()


q.join() # 这里是阻塞 主线程 ，队列没有消耗完成  不予以放行

print('淘货完成')
