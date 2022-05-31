# -*- coding: utf-8 -*-
# @Time : 2022/4/20 15:43 
# @Author : chen.zhang 
# @File : M_Clent-1.py
import socket

server_ip = '127.0.0.1'
server_port = 8888

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# client.send('一号客户端'.encode('utf-8'))
while True:
    msg = input('信息：')
    client.send(msg.encode('utf-8'))