# -*- coding: utf-8 -*-
# @Time : 2022/4/20 16:46 
# @Author : chen.zhang 
# @File : server_C1.py
import socket

server_ip = '127.0.0.1'
server_port = 8888

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# client.send('一号客户端'.encode('utf-8'))

while True:
    send_msg = input('菜品信息：')
    client.send(send_msg.encode('utf-8'))
    if send_msg == 'q':
        print('柜台下班了！')
        client.close()
        break

    recv_msg = client.recv(1024)
    print(recv_msg.decode('utf-8'))
