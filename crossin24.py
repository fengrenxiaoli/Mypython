#!/etc/bin/python3
#-*- coding:UTF-8 -*-
#先向程序输入一个值x，再输入一个值y。(x,y)表示一个点的坐标

x=int(input('输入x：'))
y=int(input('输入y：'))

if x>=0:
    if y>=0:
        print(1)
    else:
        print(2)
else:
    if y>=0:
        print(3)
    else:
        print(4)
