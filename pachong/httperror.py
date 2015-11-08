#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.request

try:
    urllib.request.urlopen('http://blog.csdn.net/cqcre')
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
