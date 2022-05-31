# -*- coding: utf-8 -*-
# @Time : 2022/4/18 16:09 
# @Author : chen.zhang 
# @File : Class_OOP_encapsulation.py

class Course:
    school = '万门'
    __totallessons = 0
    __totalincome = 0

    def __init__(self, title, duration, price, discounted=False):
        self.title = title
        self.duration = duration
        self.price = price
        self.discounter = discounted
        Course.__totallessons = Course.__totallessons + 1
        if discounted == True:
            Course.__totalincome = Course.__totalincome + self.__discount()
        else:
            Course.__totalincome = Course.__totalincome + price

    def __discount(self):
        discount_rate = 0.8
        return self.price * discount_rate

    def conyent(self, content):
        print('课程内容：', content, '时长：', self.duration)

    def pay(self):
        if self.discounter:
            print(self.__discount())
        else:
            print(self.price)

    @classmethod
    def internal_info(cls):
        print('销售额度：', cls.__totalincome, '销量：', cls.__totallessons)


py_basic = Course('py基础', 30, 199, True)
py_basic.pay()
py_basic.conyent('------------')
py_basic.internal_info()
py_basic = Course('py基础', 30, 300)
py_basic.pay()
py_basic.conyent('------------')
py_basic.internal_info()