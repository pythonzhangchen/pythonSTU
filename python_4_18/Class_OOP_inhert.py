# -*- coding: utf-8 -*-
# @Time : 2022/4/18 14:59 
# @Author : chen.zhang 
# @File : Class_OOP_inhert.py
import time


class Course:
    school = '万门'
    teachers = ['正正', '宁夫']
    __totallessons = 0

    def __init__(self, duration, title):
        self.duration = duration
        self.title = title
        Course.__totallessons = Course.__totallessons + 1
        self.OBJcreatetime = self.createtime()

    def content(self, content):
        print('课程内容：', content, '时长：', self.duration)

    def lessontime(self):
        print('开课时间周一到周五')

    @classmethod
    def total(cls):
        print('共计生产数量:', cls.__totallessons)

    @classmethod
    def addteacher(cls, teacher):
        cls.teachers = cls.teachers + teacher
        return cls.teachers

    @staticmethod
    def createtime():
        return time.ctime()


# 万门之初 1.0 模式
# 实例化
# py_basic = Course(30, 'PY基础')
# py_wb = Course(20, 'PY Web开发')
#
# # 操作类的私有属性
# Course.total()
# py_basic.total()
# # 操作类方法
# print(Course.addteacher(['培培']))
# # 类访问类属性
# print(Course.teachers)
#
#
# print(py_basic.OBJcreatetime)
# print(py_wb.OBJcreatetime)
# py_wb.lessontime()

# 万门2.0模式

class NewCourse(Course):
    def __init__(self, isCharged, Price, duration, title):
        super().__init__(duration, title)  # 超类 初始化
        # 可以使用Course.__init__(sele,duration,title)  多继承需要用这个
        self.duration = duration
        self.title = title
        self.isCharge = isCharged
        if self.isCharge == '免费课':
            self.Price = 0
        else:
            self.Price = Price

    def content(self, content):
        # super().content('棒棒哒课程，各种新奇的py玩法')  # 通过super 直接调用父类方法
        print('新时代万门课程内容', content)
        print('课程创建时间', self.createtime())  # 注意这里的继承 就自然拥有了父类的所有方法

    def access(self):
        print(self.isCharge, '支持直播和录播')


py_basic = NewCourse('收费课', 300, 30, 'py基础')
py_web = NewCourse('免费课', 0, 10, 'py Web')

py_basic.content('各种py基础入门知识')  # 子类重写了父类content方法/函数
py_basic.access()  # 子类拓展的方法
print(NewCourse.school)  # 子类使用父类的类属性
print(py_basic.Price)  # 子类的实例属性
NewCourse.total()  # 子类调用父类类属性
print(py_basic.createtime())
NewCourse.addteacher(['大咖', 'milk'])  # 添加类属性
print(NewCourse.teachers)