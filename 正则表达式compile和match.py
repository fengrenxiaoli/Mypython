#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re
#将正则表达式编译成Pattern对象
pattern=re.compile(r'rlovep')
#使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
m=pattern.match('rlovep.com')
if m:
    #使用match获得分组信息
    print(m.group())

