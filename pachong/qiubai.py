#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib
import urllib.request
import re
import time
import threading

#url
url='http://www.qiushibaike.com/hot'
#headers
header={
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
try:
    #1.Request
    req=urllib.request.Request(url,headers=header)
    #2.urlopen
    opene=urllib.request.urlopen(req)
    #3.read
    data=opene.read()
    #4.decode()
    #print(data.decode())
    pattern=re.compile('<div.*?author clearfix">.*?<h2.*?>(.*?)</h2>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items=re.findall(pattern,data.decode())
    for item in items:
        #需要排除有图片的内容
        haveImg=re.search("img",item[3])
        #需要将时间戳改成正常时间
        item2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(item[2])))
        if not haveImg:
            print(item[0],item[1],item2,item[4])
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
