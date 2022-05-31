# -*- coding: utf-8 -*-
# @Time : 2022/3/31 14:33 
# @Author : chen.zhang 
# @File : python_3_31.py

persons = [['张一', '男', 32, '重庆'], ['张二', '女', 28, '西安'], ['张三', '男', 19, '成都'], ['张四', '女', 33, '贵阳'],
           ['张五', '男', 32, '重庆']]
male = []
female = []
native_place = []
age = []
age_list = []
for per in persons:
    if '男' in per:
        male.append(per)
    elif '女' in per:
        female.append(per)
    if per[2] > 30:
        age.append(per)
    if per[-1] not in native_place:
        native_place.append(per[-1])
    age_list.append(per[2])

# print(male)
# print(female)
# print(age)
# print(native_place)
# print(age_list)
# print(max(age_list))
# print(min(age_list))

print(
    f'男生名单:{male},男生数量：{len(male)},\n女生名单：{female},女生数量：{len(female)},\n年龄大于30岁名单:{age},\n最大年龄：{max(age_list)},最小年龄：{min(age_list)},\n籍贯列表：{native_place}')

selected_list = []
candidate_list = []
audition_list = []
infos = (
    ('张晓', '男', 22, '本科', '985'),
    ('刘培', '女', 26, '硕士', '双非'),
    ('李慧', '女', 29, '本科', '211'),
    ('大黄', '男', 22, '硕士', '985'),
    ('大明', '女', 25, '硕士', '双非'),
    ('老刘', '男', 44, '本科', '985'),
    ('小A', '女', 38, '硕士', '211'),
    ('冬雪', '女', 20, '专科', '双非'),
    ('初夏', '男', 43, '硕士', '211'),
    ('晨星', '男', 35, '本科', '211'),
)

for info in infos:
    if info[3] not in '专科' and info[2] <= 30 and (info[-1] == '985' or info[-1] == '211'):
        selected_list.append(info)
    else:
        candidate_list.append(info)
print(selected_list)
print(candidate_list)