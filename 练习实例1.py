#!/etc/bin/python3
#-*- coding:UTF-8 -*-
#有1、2 、3 、4这几个数字，能组成多少个互不相同且无重复数字的三位数，都是多少
#www.runool.com python 100例

list=[1,2,3,4]
list1=[]

for x in list:
    for y in list:
        for z in list:
            if x!=y and x!=z and y!=z:
                s=x*100+y*10+z
                list1.append(s)

print(list1)
