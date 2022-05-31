# -*- coding: utf-8 -*-
# @Time : 2022/4/20 15:06 
# @Author : chen.zhang 
# @File : __init__.py.py
exam_result = {
    '张旭': '540',
    '李阳': '575',
    '王强': '583',
    '徐增': '569',
    '齐飞': '557'
}

des_order = sorted(exam_result.items(), key=lambda x: x[1], reverse=True)
print(dict(des_order))
