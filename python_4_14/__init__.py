# -*- coding: utf-8 -*-
# @Time : 2022/4/14 15:24 
# @Author : chen.zhang 
# @File : __init__.py.py
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('self:', self)

    @classmethod
    def bulid(cls):
        p = cls("tom", 18)
        print('cls:', cls)
        return p


if __name__ == '__main__':
    person = Person.bulid()
    print(person, person.name, person.age)
