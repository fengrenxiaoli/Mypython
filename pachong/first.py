#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.request

content=urllib.request.urlopen("http://www.baidu.com")
#print(content.read())
#如果直接输出就无法再写到文件里面了
x=content.read()
with open('/home/liunian/Documents/first.html','a+') as f:
    f.write(x.decode('UTF-8'))
