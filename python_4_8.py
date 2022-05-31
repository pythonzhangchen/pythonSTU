# -*- coding: utf-8 -*-
# @Time : 2022/4/8 15:44 
# @Author : chen.zhang 
# @File : python_4_8.py

# 使用一个生成器生成抽奖ID

my_gen = (x for x in range(1, 10000))

# 参加抽奖的总人数（注意这里是延申的一个设计，一会我们讲为什么）
total_p = 30

# 奖品字典 包含 奖品和奖品数量

prize_dict = {
    'iphone': 12,
    'ipad': 3,
    'macbook': 1,
    'switch': 3,
    '京东500元购物卡': 5,
    'PS4': 2
}

import random

# 用于抽奖的列表，我们叫奖池，奖池开始肯定是空的，根据我们实际情况添加
lottery_list = []


# 抽奖概率的主控函数 并且可以改变中将概率大小

def probability(num_p, dic):
    '''
    :param num_p: 公司参加与抽奖人数
    :param dic: 奖品字典，包括奖品名称和数量
    :return:
    '''
    # 这里做一级输入数据的判断，让控制函数健壮一些
    if type(num_p) != int or type(dic) != dict:
        print('您输入的参数格式不正确')
    else:
        sum_dic = 0
        # 先去遍历一下奖品字典
        for k, v in dic.items():
            # 根据字典中各个奖品的数量，将奖品添加到抽奖池列表中，改变奖品数量可以改变中将概率（奖品越多中将概率越高）
            for i in range(v):
                lottery_list.append(k)
            sum_dic += v  # 注意这里要计算一下  总奖品数量  下一步要用

            for j in range(num_p - sum_dic):
                # 根据参与抽奖总人数往抽奖池中添加数据，将总人数减去奖品数，得到的数字就是往奖品池列表添加的不中将数量，改变人数可以改变中将概率
                # 大家这么理解啊，不中将也是一种奖品，因为这个概率取决于 奖品数量和人数的差值，差值越大不中奖概率越大
                lottery_list.append('没中奖')


help(probability)

# 调用函数  传参
probability(total_p, prize_dict)

# 打乱抽奖池里面元素的顺序（这个特别重要，添加是按照顺序添加，取也是按照顺序取，所以必须要打乱）
# 这个就是**摇晃抽奖箱**的过程
# 注意 shuffle是操作原始列表，不会重新创建新的对象
random.shuffle(lottery_list)

print(lottery_list)

new_iter = iter(lottery_list)

# 注意 取得时候是从 下标/index/索引 0开始取，不是-1开始取
while 1:
    if total_p != 0:
        print('-' * 50)
        print('开始抽奖请输入"抽奖"，结束抽奖请输入结束')
        if input() == '抽奖':
            p = next(new_iter)
            total_p -= 1
            if p == '没中奖':
                print('很遗憾您没有中将')
            else:
                num = format(next(my_gen), '04d')  # 特别注意一下这里，需要通过format()函数转一下，04d:0000digit
                print('恭喜您中将了，奖品是：'+p+'，中奖ID是：'+str(num))
        elif input() == '结束':
            break
    else:
        print('抽奖次数已经用完')
        break
