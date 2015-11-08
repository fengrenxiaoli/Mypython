#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def fib(n):
	'''打印斐波那契数列'''
	a,b=0,1
	print(a)
	while a<n:
		print(b)
		a,b=b,a+b

fib(20)
print(fib.__doc__)
