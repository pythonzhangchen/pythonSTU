# -*- coding: utf-8 -*-
# @Time : 2022/4/11 17:18 
# @Author : chen.zhang 
# @File : test.py

img = [
    'aa.png',
    'bb.png',
    'cc.jpg'
]
# TODO 我要做数据训话

for file in img:
    if '.jpg' in file:
        print(file)

'''
ctrl+alt+L
'''
raw = [
    'http://www.baidu.com/index.html',
    'http://www.baidu.com/1.html',
    'http://post.baidu.com/index.html',
    'http://mp3.baidu.com/index.html',
    'http://mp3.baidu.com/3.html',
    'http://post.baidu.com/2.html',
]

result = []
for txt in raw:
    res=txt.split('/')[2]
    result.append(res)
print(max(result))
print(result.count('www.baidu.com'))