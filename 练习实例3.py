#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

'''
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少
'''

import math
'''
基本思路是先设定好完全平方数，再做判断
'''
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100) and (y*y==i+268):
        print(i)
