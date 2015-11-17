#/usr/bin/env python3
#-*- coding:utf-8 -*-


'''
斐波那契数列
'''

def fib(n):
    a,b=0,1
    l=[]
    l.append(a)
    while b<n:
        l.append(b)
        a,b=b,a+b
    print(l)

if __name__ == '__main__':
    fib(100)