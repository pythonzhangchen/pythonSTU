# -*- coding: utf-8 -*-
# @Time : 2022/4/14 16:53 
# @Author : chen.zhang 
# @File : python_4_14.py
import os

# print(os.path.abspath('utest.py')) # 获取当前文件的绝对路径
# print(os.path.isdir('C:\\Users\\it\\PycharmProjects\\pythonSTU\\python_4_12')) # 获取当前文件是否为文件夹
# print(os.path.basename('C:\\Users\\it\\PycharmProjects\\pythonSTU\\python_4_12')) # 获取当前路径的结尾名字
# print(os.path.split('C:\\Users\\it\\PycharmProjects\\pythonSTU\\python_4_12')) 以路径文件名切分成列表
# print(os.path.join('c:\\', 'python', 'test'))
# print(format(os.path.getsize('python_3_21.py') / 1024, '.2f'))  # KB

# print(os.getcwd())    # 获取当前工作绝对路径

# abs_path = os.path.abspath('python_4_14')
# for f in os.listdir(abs_path):    # 获取当前路径下所有文件/文件夹
#     # print(f)
#     file_folder = abs_path + '\\' + f
#     print(file_folder)

# os.remove('C:\\Users\\it\\PycharmProjects\\pythonSTU\\python_4_14\\abc.zip')   #删除文件
# os.rmdir('myfolder')      # 删除一个目录（目录必须要为空）

# os.removedirs('fileRemove/2/4/5')     #删除多级目录，目录必须要为空 从底层往上层全部删除

# os.mkdir('myfolder')      创建一级或多级目录
# os.makedirs('myfolder/subfoler')


import shutil

# shutil.rmtree('file_shutil_1')      # 删除目录下的多有文件、目录，无论是否有文件
# shutil.copytree('file_shutil', 'new_foler')   # 文件夹全量复制
# shutil.copy('abc.zip', 'newabc.zip')  # 文件复制
# shutil.move('abc.zip', 'fileRemove/NEWabc.zip')   # 文件夹/文件剪切

# 压缩
import zipfile

# z = zipfile.ZipFile('new.zip', 'w')
# for x in os.listdir('python_4_14'):
#     z.write('python_4_14' + os.sep + x)
# z.close()


# 上下文管理器 context manager
# with zipfile.ZipFile('new.zip', 'w') as w:
#     for x in os.listdir("python_4_14"):
#         w.write('python_4_14' + os.sep + x)


# 解压
# f = zipfile.ZipFile('new.zip', 'r')
#
# for file in f.namelist():
#     print(file)
#     f.extract(file, 'temp/')

# with zipfile.ZipFile('new.zip', 'r') as r:
#     for file in r.namelist():
#         print(file)
#         r.extract(file, 'temp/')
