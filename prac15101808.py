#!/ust/bin/env python3
# -*- charset:utf-8 -*-

import math

def mymove(x,y,step,angle=0):
    mx = x+step*math.cos(angle)
    my = y+step*math.sin(angle)
    return mx,my
