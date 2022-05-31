# -*- coding: utf-8 -*-
# @Time : 2022/4/20 15:07 
# @Author : chen.zhang 
# @File : socket_client_1.py
import socket

# Address famliy 特指IP address
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

server_ip = '127.0.0.1'  # 服务端  当前电脑的IP地址
server_port = 8888  # 这里是证书

client.connect((server_ip, server_port))

# while循环是为了保证能持续进行对话
while True:
    # 输入发送的信息
    sendmsg = input("请输入：")
    # 发送数据，以bytes字节，所有以需要进行编码
    client.send(sendmsg.encode("utf-8"))
    if sendmsg == 'q':
        # 关闭客户端
        client.close()
        break
    # 接受服务器返回的数据，需要解码
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
