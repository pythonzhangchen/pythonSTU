# -*- coding: utf-8 -*-
# @Time : 2022/4/12 17:35 
# @Author : chen.zhang 
# @File : price.py

def get_value(data, k):
    return data.get(k)


def price_score(data):
    car_by_price = sorted(data, key=lambda x: get_value(x, '售价'), reverse=False)
    score = 1
    for car_price in car_by_price:
        car_price['价格得分'] = car_price['价格得分'] + score
        score += 1
    return car_by_price
