# -*- coding: utf-8 -*-
# @Time : 2022/3/21 16:41 
# @Author : chen.zhang 
# @File : python_3_21.py


# 猜价格
# 第一种写法
my_price = 100
while True:
    guess_price = input("你猜多少money：")
    if str(my_price) == guess_price:
        print('猜对了')
        break
    else:
        print('再来一次吧')

# 第二种写法
my_price = 100
status = True
while status:
    guess_price = input("你猜多少money：")
    if str(my_price) == guess_price:
        print('猜对了')
        status = False
    else:
        print('再来一次吧')

#  做一个v模拟登录
username = 'gz'
password = '123'
while True:
    login_user = input("请输入用户名:")
    login_pwd = input('请输入密码:')
    if login_user == username and login_pwd == password:
        print("登录成功！ 欢迎来到万门大学VIP中心")
        break
    else:
        print('用户名或密码不正确')

# 投币猜数字小游戏
import time
import random

number = random.randint(10, 99)

money = 10

while money > 0:
    time.sleep(1)
    guess_number = int(input('请输入你猜的数字:->'))
    if number > guess_number:
        money = money - 2
        print('******猜小了哦，你还剩', money, '个币', '还有', int(money / 2), '次机会啦******')
    elif number < guess_number:
        money -= 2
        print('******猜大了哦，你还剩', money, '个币', '还有', int(money / 2), '次机会啦******')
    else:
        print('******BINGO! 你真棒！猜对了！奖励你10个币，继续玩吧')
        money -= 2
        money += 10
        print('****你现在有', money, '个币了，继续玩吧！****')
        #  充值随机数答案，继续玩
        number = random.randint(10, 99)

if money == 0:
    print('*****抱歉，你的币用光啦~问妈妈要钱，区买币吧：（******')
    print('真正的答案是：', number)
