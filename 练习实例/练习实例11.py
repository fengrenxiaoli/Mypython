#/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
斐波那契数列
'''

l=[]
a,b=0,1
l.append(b)
while b<10000000:
    l.append(b)
    a,b=b,a+b

print(l)
