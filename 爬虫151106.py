#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re
import urllib.request
import urllib

from collections import deque
#使用队列存放url
queue=deque()

#使用visited防止重复爬同一页面
visited=set()

url='https://book.douban.com/top250'
#入队最初的页面
queue.append(url)
cnt=0

while queue:
    url=queue.popleft()
    visited |={url}     #标记已访问页面

    print('已经抓取:'+str(cnt)+'    正在抓取 '+url)
    cnt+=1
    #抓取页面
    urlop=urllib.request.urlopen(url)
    #判断是否为html页面
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    #避免程序异常中止，用try...catch处理异常
    try:
        #转换为utf-8码
        data=urlop.read().decode('utf-8')
    except:
        continue

    #正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列
    linkre=re.compile("href=['\"]([^\"'>]*?)['\"].*?")
    for x in linkre.findall(data):    #返回所有有匹配的列表
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列---->'+x)
