# -*- coding: utf-8 -*-
# @Time : 2022/4/14 15:25 
# @Author : chen.zhang 
# @File : bugsDemo.py

def showdata(start, end):
    l = [1, 2, 3, 'a', 5]
    try:
        for i in range(start, end):
            print(l[i])
            print('我的数字：%d' % l[i])
    except IndexError as e:
        print('异常信息：', e)
        print('超出列表范围')
    except TypeError as e:
        print(e)
        print('类型错误')
    except Exception as e:
        print('其它错误：', e)
    else:
        print('看来你的程序成功运行了')
    finally:
        print('无论成败我都会执行')


showdata(0, 10)
