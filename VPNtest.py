# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:54:57 2019

@author: qwh_1
"""

import requests

#测试墙内域名
#url='http://www.baidu.com'

#测试墙外域名
url='https://www.google.com/'

#IP查询
url='http://ip.chinaz.com/'

#设置代理端口
proxies = {'https': 'https://127.0.0.1:1080', 'http': 'http://127.0.0.1:1080'}

#使用代理
res=requests.get(url, proxies=proxies, verify=False)

#不使用代理
res=requests.get(url, proxies=False, verify=False)

if(res.status_code==200):
    print('翻墙成功')
else:
    print('翻墙失败')
