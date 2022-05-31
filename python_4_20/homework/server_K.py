# -*- coding: utf-8 -*-
# @Time : 2022/4/20 16:46 
# @Author : chen.zhang 
# @File : server_C1.py
import socket
import threading

server_ip = '127.0.0.1'
server_port = 8888

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen()
print(f'服务器端启动IP：{server_ip}')

# 创建里两个函数  一个负责 与 客户端沟通 ， 一个负责创建多线程


###----------------------------管理用途 全局变量--------------------------
order = {}  # 存储菜品和client映射关系{clientOBJ:[1,2,3]}


###--------------------------------------------------------------------

def client_connection(connection, address):
    print(f'柜台上线，接入地址为{address}')
    print(f'柜台上线    {connection}')
    while True:
        msg = connection.recv(15).decode('utf-8')
        order[connection].append(msg)  # 特别注意，遇到q不添加
        print(msg)
        if msg == 'q':
            print('柜台下线')
            break
        connection.send('后厨收到'.encode('utf-8'))  # 自动返回一个数据给柜台
    connection.close()


def server_control():
    global server, order
    while True:
        connection, address = server.accept()
        order[connection] = []
        c_thread = threading.Thread(target=client_connection, args=(connection, address))
        c_thread.start()
        print('总在线柜台数：%s' % (threading.activeCount() - 2))  # 注意这里是减除了主线程/管理线程，获得子线程总量即客户端量


print('后厨已经上线....开始接餐....')
T1 = threading.Thread(target=server_control)
T1.start()

while True:
    print("请输入查询命令：1查询所有订单 2查询在线柜台数量 3完成处理 4系统通知")
    command = input()
    # 查看字典的所有value
    if command == '1':
        print(order.values())
    # 查看当前所有的在线数量
    elif command == '2':
        print('总在线柜台数：%s' % (threading.activeCount() - 2))
    elif command == '3':
        done_order = input('请输入已经完成的菜品：：')
        for k, v in order.items():
            if done_order in v:
                k.send(f'菜品：{v}已经完成'.encode('utf-8'))
    elif command == '4':
        for k, _ in order.items():  # _ 当数据不准备使用的时候 _ 表示
            k.send('来自后台的公共信息！全家桶没有了'.encode('utf-8'))
