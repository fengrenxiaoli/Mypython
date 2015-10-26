#!/usr/bin/env python
#-*- coding:utf-8 -*-

def test():
    print('Guess what I think?')
    s=10
    x=int(input())
    while True:
        if x<s:
            print('Your answer is too small')
            x=int(input())
        elif x>s:
            print('Your answer is too large')
            x=int(input())
        else:
            print('BINGO!!!')
            break
test()
