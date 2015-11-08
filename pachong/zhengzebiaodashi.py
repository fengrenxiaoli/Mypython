#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='lili'

import re

pattern=re.compile(r'hello')

re1=re.match(pattern,'hello')
re2=re.match(pattern,'hellooo')
re3=re.match(pattern,'helo')
re4=re.match(pattern,'hello xxxx')

if re1:
    print(re1.group())
else:
    print('1匹配失败')

if re2:
    print(re2.group())
else:
    print('2匹配失败')

if re3:
    print(re3.group())
else:
    print('3匹配失败')

if re4:
    print(re4.group())
else:
    print('4匹配失败')

print('\n')

search=re.search(pattern,'world hello')
print(search.group())

pattern1=re.compile(r'\d')
print(re.split(pattern1,'one1two2three3four4'))
