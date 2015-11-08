#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.request
import http.cookiejar

#声明一个CookieJar对象实例来保存cookie
cookie=http.cookiejar.CookieJar()
#利用HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
for item in cookie:
    print('Name='+item.name)
    print('Value='+item.value)
