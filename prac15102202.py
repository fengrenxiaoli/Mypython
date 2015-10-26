#!/usr/bin/env/ python
#-*- coding:utf-8 -*-

__author__='Lee'

import os
for root,dirs,files in os.walk('e:\\github\python'):
    open('files.txt','a').write("%s %s %s"%(root,dirs,files))


