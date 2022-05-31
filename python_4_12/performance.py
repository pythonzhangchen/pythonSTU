# -*- coding: utf-8 -*-
# @Time : 2022/4/12 17:35 
# @Author : chen.zhang 
# @File : performance.py

def get_value(data, k):
    return data.get(k)


def by_performance(data, *args):
    for y in args:
        car_by_performance = sorted(data, key=lambda x: get_value(x, y))
        score = 1
        for car_performance in car_by_performance:
            car_performance['性能得分'] = car_performance['性能得分'] + score
            score += 1
    return car_by_performance
