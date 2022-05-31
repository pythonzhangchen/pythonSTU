# -*- coding: utf-8 -*-
# @Time : 2022/4/20 15:07 
# @Author : chen.zhang 
# @File : socket_client_1.py
import socket

# Address famliy 特指IP address
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip_addr = '127.0.0.1'  # 服务端  当前电脑的IP地址
port = 8888  # 这里是证书

server.bind((ip_addr, port))  # 特别注意这里要传一个tuple元组
server.listen(5)  # 这里设置监听，参数代表监听数量，换句话说就是允许多少client接入

# 当前接入client的socket对象，当前接入client的ip地址和端口

print(f'服务器启动...正在聆听你们的声音...服务器端IP：{ip_addr}')
# 建立 等待接收  进入的 客户端 client
client, addr = server.accept()

# 特别注意种类的while 是让sever持续在线（监听状态），保证不退出
while True:
    # 接收客户端的请求
    recvmsg = client.recv(1024)  # 注意这里特质了可以接受的数据量
    # 把接受到的数据进行解码
    # if recvmsg： # 空不执行
    strDate = recvmsg.decode("utf-8")  # 注意这里需要decode，从bytes字节 解码 utf-8
    print(strDate)
    # 判断客户端是否发送q,是就退出，关闭服务器
    if strDate == 'q':
        client.send('服务器已经关闭！'.encode('utf-8'))
        server.close()
        break
    # print("收到：" + strData)
    # msg = input("回复：")
    # 对要发送的数据进行编码
    client.send(f'服务器收到你的信息！{strDate}'.encode("utf-8"))
    # client.send(msg.encode("utf-8"))  # 把utf-8 编码bytes 字节发送
