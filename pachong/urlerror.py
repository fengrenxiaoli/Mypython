#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.request

try:
    urllib.request.urlopen('http://www.xxxxxx.com')
except urllib.error.URLError as e:
    print(e.reason)
