# -*- coding: utf-8 -*-
# @Time : 2022/4/13 9:59 
# @Author : chen.zhang 
# @File : python_4_13.py
import re

# 普通字符，所见即所得
txt = '万门大学'
patt = r'万门'
res = re.findall(pattern=patt, string=txt)
# print(res)

# 特殊字符表达式，精髓
patt = r'.'
res = re.findall(pattern=patt, string=txt)
# print(res)

txt = '''
我在万门学python
我在万门学Django
我在万门学Java
我在万门学PPT
我在万门学
'''

patt = re.compile(r'学.+|学.*')  # 注意compile编辑的意思，这里是编译当前的表达式
res = patt.findall(txt)
# print(res)

txt = '''
我市你的正正老师
13800001111
13300001111
13400
136123123
1510000134
万门大学
.*.*&#$
'''

patt = r'.{2,3}'
res = re.findall(pattern=patt, string=txt)
# print(res)


txt = '''
张三 python工程师
李四 java工程师
王五五 前端工程师
'''
patt = r'^.{2,3}'
# finall()函数的参数 re.M = Multilines 多行取法，就是一行一组取
res = re.findall(pattern=patt, string=txt, flags=re.M)
# res = re.findall(patt, txt, re.M)
# print(res)


txt = '''
张三 python工程师 8000
李四 java工程师 10000
王五五 前端工程师 12000
'''
# patt = r'.{5}$'
# res = re.findall(patt,txt,re.M)

patt = r'\d+$'
res = re.findall(patt, txt, re.M)
# print(res)

txt = '''
张三,销售总监,5000,3000
李四,销售经理,4000,2000
王五五,渠道经理,3500,1000
'''

patt = r',(\d+),(\d+)'
res = re.findall(patt, txt, re.M)
# print(res)


phone = '''
12300001111
13900004321
15212341234
14100001234
12900003333
1c200005678
'''
patt = r'1[3,5,8]\d{9}'
res = re.findall(patt, phone)
# print(res)


words = '''
Air
Business
strange
python
java
english
England
China
'''
patt = r'^[a-eA-E].+'
res = re.findall(patt, words, re.M)
# print(res)

words = ' abs apple bus study actor great Air Business strange english England China'
patt = r' [a-eA-E]\w+'
res = re.findall(patt, words)
# print(res)

msg = '''我到万门
大学学习python
'''
patt = r'到.*学'
# 爬虫常用参数。因为在一个页面里回车非常多，如果不用re.S很多数据取不到
res = re.findall(patt, msg, re.S)
# print(res)

words = '''我是 来自 一个 万门 大学 的 对P ython 感兴趣的
纯爷们 或 小姐姐'''

patt = r'\S+'
res = re.findall(patt, words)
#  合并列表
newres = ''.join(res)
# print(res)
# print(newres)


txt = '''
北京程序员工资10000元/月
上海程序员工资12000块/月
深圳程序员工资9500圆/月
'''
patt = r'\d+元|\d+圆|\d+块'
res = re.findall(patt, txt, re.M)
# print(res)

html = '<html><header><title>万门大学</title></header></html><body><h1>Hello world</h1></body>'
# patt = r'<(.*)>'
patt = r'<(.*?)>'
res = re.findall(patt, html)
# print(res)

html = '''
<html>
<header>
    <title>万门大学</title>
</header>

</html>

<body>
    <h1>Hello world</h1>
</body>
'''
patt = r'<(.*?)>'
res = re.findall(patt, html)
# print(res)

qq = '1234@qq.com*45532441@qq.com/4134abc234@qq.com a123324844@qq.com&15532441@qq.com#14532433@qq.com'
patt = r'[*/&# ]'
res = re.split(patt, qq)
print(res)
qqpatt = r'[1-9][0-9]{4,10}@qq.com'
qqres = re.match(qqpatt, res[-2])
print(qqres)
# 我们把它做完整

for i in res:
    if re.match(qqpatt, i):
        print(i, '合法qq号')
    else:
        print(i, '不合法qq号')

mail = 'aaa@qq.cn bb@wanmen.org ccc@cc.com '
patt = r'@.*\.\w+'
res = re.findall(patt, mail)
# print(res)

patt = r'^a[1,2]$'
res = re.match(patt, 'a1')
# print(res)


p_data = '''
1340001111
15683O39101
12301012222
19901015145
18801018492
11956110949
_dhadj@asdf.com
Abcdd.aa@abc.com
wanmen@wanmen.org
.aabbcc@166.com
zz_abc@@qq.com
'''
list_p_data = p_data.split()
for i in list_p_data:
    if re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', i):
        print(i, '合法手机号')
    elif re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', i):
        print(i, '合法邮箱')

h_data = '''
<li><a href='http://www.xiaole8.com/qgwz/'>情感文章</a></li>
<li><a href='http://www.xiaole8.com/shangganwenzhang/'>伤感文章</a></li>
<li><a href='http://www.xiaole8.com/aiqingwenzhang/'>爱情文章</a></li>
<li><a href='http://www.xiaole8.com/ganrengushi/'>感人故事</a></li>
<li><a href='http://www.xiaole8.com/qingganmw/'>情感美文</a></li>
<li><a href='http://www.xiaole8.com/lizhiwenzhang/'>励志文章</a></li>
<li><a href='http://www.xiaole8.com/renshengzheli/'>人生哲理</a></li>
<li><a href='http://www.xiaole8.com/gaoxiaowenzhang/'>搞笑文章</a></li>
<li><a href='http://www.xiaole8.com/rizhiwenzhang/'>经典文章</a></li>
<li><a href='http://www.xiaole8.com/qinqingwz/'>亲情文章</a></li>
<li><a href='http://www.xiaole8.com/youqingwz/'>友情文章</a></li>
'''
list_h_data = h_data.split('\n')
dic = {}
for i in list_h_data:
    res = re.findall(r"<li><a href='(.*?)'>(.*?)</a></li>", i)
    if len(res) > 0:
        dic[res[0][1]] = res[0][0]
#
print(dic)
