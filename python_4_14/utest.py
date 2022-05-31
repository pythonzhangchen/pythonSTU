# -*- coding: utf-8 -*-
# @Time : 2022/4/14 15:35 
# @Author : chen.zhang 
# @File : utest.py
import unittest
import test_cases


# def add():
#     return 1 + 1
#
#
# def multi():
#     return 1 * 1


class myTest(unittest.TestCase):
    def setUp(self) -> None:
        print('测试启动')

    def test_add(self):
        self.assertEqual(test_cases.add(), 4, '加法计算错误！')

    def test_mul(self):
        self.assertEqual(test_cases.multi(), 6, '乘法计算错误')

    def tearDown(self) -> None:
        print('测试结束')


if __name__ == '__main__':
    # 实例化用例套件
    suite = unittest.TestSuite()

    # 向套件里（测试集）添加测试用例
    suite.addTest(myTest('test_add'))
    suite.addTest(myTest('test_mul'))

    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)
