#/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
输入三个整数x，y，z，请把这三个整数由小到大输出
'''

def sortint(x,y):
    if x>y:
        x,y=y,x
    return x,y

if __name__ == '__main__':
    x=int(input('x:'))
    y=int(input('y:'))
    z=int(input('z:'))
    x,y=sortint(x,y)
    x,z=sortint(x,z)
    y,z=sortint(y,z)
    print(x,y,z)