#!/ust/bin/env python3
# -*- charset:utf-8 -*-

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise(TypeError('bad operand type'))
    if x>=0:
        x=x
    else:
        x=-x
    return x
print(my_abs(-2))
