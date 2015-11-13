#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
输入某年某月某日，判断这一天是这一年的第几天
'''

year=int(input('year:'))
month=int(input('month:'))
day=int(input('day:'))

x=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=0

if month>13 or month<0:
    print('month is error')
else:
    for i in range(month):
        sum+=x[i]
    sum+=day
    if month>2 and year%400==0 or year%100!=0 and year%4==0:
        sum=sum+1
print(sum)
