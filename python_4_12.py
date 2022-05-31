# -*- coding: utf-8 -*-
# @Time : 2022/4/12 17:10 
# @Author : chen.zhang 
# @File : python_4_12.py
from python_4_12 import price, effective, performance

cars_list = []
raw = open('cars.txt', 'r', encoding='UTF-8')
for x in raw.readlines():
    car_detial = {'价格得分': 0, '性能得分': 0, '性价比得分': 0, '品牌': x.split()[0], '型号': x.split()[1], '售价': x.split()[2],
                  '续航': x.split()[3], '电池容量': x.split()[4]}

    cars_list.append(car_detial)
raw.close()

# 获得 价格分数
cars_list = price.price_score(cars_list)
# for x in cars_list:
#     print(x)
# 获得 性能比较
cars_list = performance.by_performance(cars_list, '续航', '电池容量')
# for x in cars_list:
#     print(x)

result = effective.proceByPerformance(cars_list)
for x in result:
    print(x)