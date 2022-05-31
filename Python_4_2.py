# -*- coding: utf-8 -*-
# @Time : 2022/4/2 16:02 
# @Author : chen.zhang 
# @File : Python_4_2.py
# school = ['Python基础', 'Python爬虫', 'Java编程', 'Java Web', 'Python数据分析']
# condition = lambda x: True if 'Python' in x else False
#
#
# def keyword_search(keys, func):
#     search_result = []
#     for result in keys:
#         if func(result):
#             search_result.append(result)
#     return search_result
#
#
# print(keyword_search(school, condition))
#
#

import xlrd

book = xlrd.open_workbook(r'C:\Users\it\Desktop\city_data.xlsx')
sheet = book.sheet_by_index(0)

main_data_list = []

for row in range(3, sheet.nrows):
    temp_dict = {}
    # print(sheet.row_values(row))
    temp_dict['城市'] = sheet.row_values(row)[0]
    temp_dict['2019GDP'] = sheet.row_values(row)[1]
    temp_dict['2018总人口'] = sheet.row_values(row)[2]
    temp_dict['2018平均房价'] = sheet.row_values(row)[3]
    temp_dict['2018平均工资'] = sheet.row_values(row)[4]
    temp_dict['地铁总里程'] = sheet.row_values(row)[5]
    temp_dict['高校数量'] = sheet.row_values(row)[6]
    temp_dict['三甲医院数量'] = sheet.row_values(row)[7]
    temp_dict['2018小学生数量'] = sheet.row_values(row)[8]
    main_data_list.append(temp_dict)


def get_value(dic, k):
    return dic.get(k)  # dict.get和dict[]取值二者有什么区别  前者没找到什么都不干，后者没找到会直接报错


def desc_cities(cities_list, kw='2019GDP'):
    if kw != '2018平均房价':
        cities_by_key = sorted(cities_list, key=lambda x: get_value(x, kw), reverse=True)
        print(cities_by_key)
        for i_key in range(len(cities_by_key)):
            cities_by_key[i_key][kw + '得分'] = len(cities_by_key) - i_key
        print(f'城市{kw}得分（由高到低）：')
        for j_key in range(len(cities_by_key)):
            print(cities_by_key[j_key]['城市'], cities_by_key[j_key][kw + '得分'])
        print('-' * 80)
    else:
        cities_by_key = sorted(cities_list, key=lambda x: get_value(x, kw), reverse=True)
        for i_house in range(len(cities_by_key)):
            cities_by_key[i_house][kw + '得分'] = i_house + 1
        print(f'城市{kw}得分（由高到低）：')
        for j_house in range(len(cities_by_key)):
            print(cities_by_key[j_house]['城市'], cities_by_key[j_house][kw + '得分'])
        print('-' * 80)
    return cities_by_key


desc_cities(main_data_list, '2019GDP')
desc_cities(main_data_list, '2018平均房价')
# desc_cities(main_data_list, '地铁总里程')
# desc_cities(main_data_list, '高校数量')
# cities_bykey=desc_cities(main_data_list, '2018小学生数量')
# print(main_data_list)
