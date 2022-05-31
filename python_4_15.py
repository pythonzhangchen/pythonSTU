# -*- coding: utf-8 -*-
# @Time : 2022/4/15 16:40 
# @Author : chen.zhang 
# @File : python_4_15.py

# 1、使用os、shutil和zipfile完成该任务
# 2、要求对文件进行判断,大于10MB
# 3、满足文件大小，然后复制文件到统一的目录
# 4、把该目录下的文件进行zip压缩保存
import os, shutil

folder = 'c:\\pythonClass\\家庭作业\\files'


# 递归算法，自己调用自己

def find_files(path):
    dirs = []
    # 先去找目录
    for file in os.listdir(path):
        print(file, os.path.join(path, file))
        # 如果市目录添加到dirs列表中
        if os.path.isdir(os.path.join(path, file)):
            print(file)
            dirs.append(os.path.join(path, file))
        else:  # 如果不是目录 即文件，那么我们再处理下边的判断
            file_size_MB = os.path.getsize(os.path.join(path, file)) / 1024 / 1024
            if file_size_MB > 10:
                shutil.copy(os.path.join(path, file), 'myNewFile')
    # 从dirs遍历文件/文件夹，再调用自己
    for i in dirs:
        find_files(i)


find_files(folder)

# import zipfile
#
# with zipfile.ZipFile('NEW.zip', 'w') as w:
#     for file in os.listdir('myNewFiles'):
#         w.write(os.path.join('myNewFiles', file))
