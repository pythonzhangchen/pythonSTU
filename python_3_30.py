# -*- coding: utf-8 -*-
# @Time : 2022/3/30 11:16 
# @Author : chen.zhang 
# @File : python_3_30.py

import string
import random

#   打印出8位随机码
code = ''.join(random.sample(string.digits + string.ascii_lowercase, 8))
print(code)


help(range)