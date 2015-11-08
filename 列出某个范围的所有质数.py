#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
定义判断一个数是否是质数的函数
'''
def iszhishu(x):
    if x<0:
        print(x,'is 负数')
        return False
    if x==0:
        return False
    if x==1|x==2:
        return True
    for n in range(2,x):
        if x%n==0:
            return False
    else:
        return True

def setofzhishu(x):
    a=[]
    for i in range(0,x):
        if iszhishu(i):
            a.append(i)
    print(a)

inputx=int(input('输入一个数：'))
setofzhishu(inputx)
