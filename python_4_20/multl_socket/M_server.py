# -*- coding: utf-8 -*-
# @Time : 2022/4/20 15:43 
# @Author : chen.zhang 
# @File : M_server.py.py
import socket, threading

# Address famliy 特指IP address
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip_addr = '127.0.0.1'  # 服务端  当前电脑的IP地址
port = 8888  # 这里是证书

server.bind((ip_addr, port))  # 特别注意这里要传一个tuple元组
server.listen()  # 这里设置监听，参数代表监听数量，换句话说就是允许多少client接入

# 当前接入client的socket对象，当前接入client的ip地址和端口

print(f'服务器启动IP：{ip_addr}')


# 创建里两个函数 一个负责 与 客户端沟通， 一个负责创建多线程

def client_connection(connection, address):
    print(f'新客户端接入,接入地址为{address}')

    while True:
        msg = connection.recv(10).decode('utf-8')
        print(msg)
        if msg == 'q':
            break
    connection.close()



def server_control():
    global server
    while True:
        connection, address = server.accept()
        c_thread = threading.Thread(target=client_connection, args=(connection, address))
        c_thread.start()
        print('总在线用量 %s' % (threading.activeCount() - 1))  # 注意这里是减除主线程，获得子线程总量即客户端量


print('服务器已经上线...等待接入....')
server_control()
