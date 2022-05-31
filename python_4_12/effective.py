# -*- coding: utf-8 -*-
# @Time : 2022/4/12 17:35 
# @Author : chen.zhang 
# @File : effective.py
def get_value(data, k):
    return data.get(k)


def proceByPerformance(data):
    for info in data:
        info['性价比得分'] = float(format(info['性能得分'] / info['价格得分'], '.2f'))
    final_result = sorted(data, key=lambda x: get_value(x, '性价比得分'), reverse=True)
    return final_result
