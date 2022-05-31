# -*- coding: utf-8 -*-
# @Time : 2022/4/27 16:59 
# @Author : chen.zhang 
# @File : shevle_pickie.py
import pickle

a = 123123.0

with open('plk_she/a.plk', 'wb') as w:  # wb wirte binary  写入二进制
    pickle.dump(a, w)

# 读取pickle持久化
with open('plk_she/a.plk', 'rb') as r:
    data = pickle.load(r)
    print(type(data))
    print(data)

# def cal(a,b):
#     return a+b
#
# cal_func= cal
#
# # -----函数对象保存
# # 写入pickle持久化 就是保存
# with open('plk_she/a.plk','wb') as w:
#     pickle.dump(cal_func,w)
#
# with open('plk_she/a.plk','rb') as r:
#     data= pickle.load(r)
#     print(type(data))
#     print(data(1,2))


# 创建一个shelve 持久化对象， 注意这个是一种结构化，可以对结构化数据进行修改
# import shelve
#
# shv = shelve.open(r'plk_she/OSStask.db')
# shv['a'] = [1, 2, 3]
# shv['b'] = [3, 2, 1]
# shv.sync()
# shv.close()
# # 对shelve内的对象进行修改或添加
# s1 = shelve.open('plk_she/OSStask.db', writeback=True)
# del s1['a']
# s1['b'] = 'zzzzz'
# for x, y in s1.items():
#     print(x, y)
# s1.close()
