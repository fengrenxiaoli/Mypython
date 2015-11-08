#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from http import cookiejar
from urllib import request

cookie=cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(req)
request=opener.open('http://www.baidu.com')
print(request.read())