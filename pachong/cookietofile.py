#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from http import cookiejar 
import urllib.request


filename='cookie.txt'
cookie=cookiejar.MozillaCookieJar(filename)
hanlder=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(hanlder)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
