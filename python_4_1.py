# -*- coding: utf-8 -*-
# @Time : 2022/4/1 15:56 
# @Author : chen.zhang 
# @File : python_4——1.py


pass_score_dic = {}  # 过分数线名单
pass_list = []  # 最终录取名单


def enroll_list(university, major, pass_score=550, pass_count=10, *args, **kwargs):
    '''
    函数参数说明
    :param university:大学名称 ****关键字参数
    :param major: 专业****关键字参数
    :param pass_score: ****默参
    :param pass_count: ****默参
    :param args: ****可变参数-不确定数量
    :param kwargs: ****默参可变关键字-不确定考生名字和成绩
    :return:
    '''
    global pass_score_dic, pass_list
    if len(kwargs) > 0:
        for stu, score in kwargs.items():
            if int(score) > pass_score:
                pass_score_dic[stu] = int(score)
        dic_desc = sorted(pass_score_dic.items(), key=lambda k: k[1], reverse=True)
        print('**演示输出排序输出**：', dic_desc, '\n')
        for stu_pass in dic_desc[:pass_count]:
            pass_list.append(stu_pass)
        print(f'学效：,{university};\n专业：{major};\n录取分数线：{pass_score};\n招生人数：{pass_count};\n招生老师：{args};\n考生名单及分数：{kwargs}'
              f';\n报考人数：{len(kwargs)};\n达线人数：{len(dic_desc)};\n录取名单：{pass_list};\n录取人数：{len(pass_list)}')


enroll_list('西北大学', '计算机科学', 550, 3, '张老师', '王老师', '李老师', 张旭='540', 李阳='575', 王强='583', 徐增='569', 齐飞='557')


