#/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
暂停一秒输出
'''
import time

dictx={'a':'10','b':'12'}
for key,value in dictx.items():
    print(key,value)
    time.sleep(2)