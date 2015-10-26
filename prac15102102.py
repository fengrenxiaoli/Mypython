#!/usr/bin/env python3
# -*- charset:utf-8 -*-

def sushu(n):
    if n==1|n==2:
        return True
    else:
        for(i=2,i<n,i++):
            if n%i==0:
                return False
        return True

i=0
while i<=100:
    if sushu(i):
        print(i+'\t')
    i++
