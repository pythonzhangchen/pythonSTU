# -*- coding: utf-8 -*-
# @Time : 2022/4/7 15:42 
# @Author : chen.zhang 
# @File : python_4_7.py

# 装饰器本身是一个函数，那么装饰器去装饰另一个函数的时候，原有函数就会“消逝”
# 为了避免让这个“最头部”的函数（被装饰的函数）不消失，可以使用wraps函数，它的作用是保证被修饰函数名不被变化
# 注意wraps函数是追溯上一函数名字，所以如果有多个装饰器，那么每个装饰器都要有，这条线不能断！

login_status = False
log = []
prohibit_list = ['枪支', '弹药', '药品', '野生动物']
super_adm = {'user': 'peipei', 'pwd': '123456'}
product = {}



import time
from functools import wraps


# 登录功能装饰器
def login(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        global login_status, super_adm
        if login_status == True:
            return func(*args, **kwargs)
        else:
            login_user = input('请输入用户名：')
            login_pwd = input('请输入密码：')
            if login_user == super_adm['user'] and login_pwd == super_adm['pwd']:
                login_status = True
                return func(*args, **kwargs)
            else:
                print('登录失败，账户或密码或身份错误')

    return wrapper_func


# 操作时间和操作用户日期装饰器
def log_write(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        global log, super_adm
        log_dic = {}
        log_dic['用户名'] = super_adm['user']
        log_dic['登录时间'] = time.strftime('%Y-%m-d %H:%M:%S', time.localtime())
        log_dic['操作类型'] = wrapper_func.__name__
        log_dic['操作内容'] = args
        log.append(log_dic)
        return func(*args, **kwargs)

    return wrapper_func


# 判断是否有违禁物品装饰器
def is_prohibit(func):
    @wraps(func)
    def wrapper_func(product_name, product_stock_num):
        global prohibit_status
        if product_name in prohibit_list:
            print('您添加的商品属于违禁商品！禁止添加')
        else:
            return func(product_name, product_stock_num)

    return wrapper_func


# 增加商品并入库
# @login
@log_write
@is_prohibit
def add_product_stock(product_name, product_stock_num):
    global product
    if product_name in product.keys():
        product[product_name] = product[product_name] + product_stock_num
    else:
        product[product_name] = product_stock_num


# 销售某商品
@log_write
def sale_product(product_name, product_sale_num):
    global product
    if product_name not in product.keys():
        print('您的销售商品不存在')
    elif product[product_name] < product_sale_num:
        print('对不起！库存不足！')
    else:
        product[product_name] = product[product_name] - product_sale_num


# 查询商品库存
# @login
@log_write
def query_product(product_name):
    if product_name not in product.keys():
        print('您查询的商品不存在')
    else:
        produc_stock = product[product_name]
        print(product_name, '的库存是：', produc_stock)


@login
def main():
    functions = {
        '1': add_product_stock,
        '2': sale_product,
        '3': query_product
    }
    func_choice = input('请输入功能编号---：')
    if func_choice == '1':
        product_name = input('请输入入库产品名称：')
        stock_num = input('请输入入库产品数量：')
        functions.get(func_choice)(product_name, stock_num)
    elif func_choice == '2':
        product_name = input('请输入销售产品名称：')
        product_sale_num = int(input('请输入销售产品数量：'))
        functions.get(func_choice)(product_name, product_sale_num)
    elif func_choice == '3':
        product_name = input('请输入查询产品名称：')
        functions.get(func_choice)(product_name)


# 我们学的越来越多__name__ __main__是什么意思？
# 这个部分是一个关于python解释器需要判断的一个东西
# 当前运行的程序作为主程序运行，而不是来自其它文件（py）的调用来运行本程序
if __name__ == '__main__':
    main()
    print(login_status, log, product, sep='\n')
