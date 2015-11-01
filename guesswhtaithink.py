#!/etc/bin/python3
#-*- coding:UTF-8 -*-

from random import randint

def isEqual(x,y):
    if x>y:
        print('too large')
        return False
    if x<y:
        print('too small')
        return False
    if x==y:
        print('Bingo')
        return True

num=randint(0,100)
print('Guess what I think?')
isbingo=False
while not isbingo:
    x=int(input())
    isbingo=isEqual(x,num)


    
