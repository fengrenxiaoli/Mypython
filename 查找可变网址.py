#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib
import urllib.request

data={}
data['word']='one peace'
url_value=urllib.parse.urlencode(data)
url='http://www.baidu.com/s?'
full_url=url+url_value
a=urllib.request.urlopen(full_url)
data=a.read()
data=data.decode('UTF-8')
print(data)
a.geturl()
