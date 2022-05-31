# -*- coding: utf-8 -*-
# @Time : 2022/4/18 15:35 
# @Author : chen.zhang 
# @File : Class_OOP_ploymorphic.py
import random


class Member:
    def __init__(self, name, age, region):
        self.name = name
        self.age = age
        self.region = region

    def create_id(self):
        return random.randint(10000, 99999)

    def whoami(self):  # 关键点 这个方法将被 子类重写
        pass
    # raise NotImplementedError('请通过具体子类方法执行') # 形成抽象类，就不再具体做任何事情了
    # 注意这里 可以用print，但是 print以后还是会继续执行程序，rasie是报错，终止程序


class VIP(Member):
    def __init__(self, name, age, region):
        self.name = name
        self.age = age
        self.region = region

    def whoami(self):
        my_id = self.create_id()
        print('我是VIP会员，我的会员id：%s' % my_id)


class Non_VIP(Member):
    def __init__(self, name, age, region):
        self.name = name
        self.age = age
        self.region = region

    def whoami(self):
        my_id = self.create_id()
        print('我是普通会员，我的会员id：%s' % my_id)


class SinglelessinMember(Member):
    def __init__(self, name, age, region):
        self.name = name
        self.age = age
        self.region = region

    def whoami(self):
        my_id = self.create_id()
        print('我是单课会员，我的会员id：%s' % my_id)


mike = Non_VIP('zz', 30, '北京')
lucy = VIP('zz', 23, '上海')
lily = SinglelessinMember('lily', 28, '厦门')


def userCheck(obj):
    obj.whoami()


userCheck(lily)

####--------
objs = [lucy, lily, mike]
for i in objs:
    i.whoami()
