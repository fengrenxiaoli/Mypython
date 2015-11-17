#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib
import urllib.request
import re
import time
import threading

'''
基本思路：
    1、初始化，定义变量
    2、传入某一页的索引获得页面代码
    3、传入某一页代码，返回本页不带图片的段子列表
    4、加载并提取页面的内容，加入到列表中
    5、调用该方法，每次敲回车打印输出一个段子
'''
class QSBk:

    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex=1
        #初始化headers
        self.user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'
        self.headers={'User-Agent' : self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories=[]
        #存放程序是否继续运行的变量
        self.enable=False

    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url='http://www.qiushibaike.com/hot/page/'+str(pageIndex)
            #1.Request
            req=urllib.request.Request(url,headers=self.headers)
            #2.urlopen
            opene=urllib.request.urlopen(req)
            #3.read & decode
            data=opene.read().decode('utf-8')
            return data
            
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print(u'连接糗事百科失败，错误原因：',e.reason)

    #传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        data=self.getPage(pageIndex)
        if not data:
            print('页面加载失败')
            return None
        pattern=re.compile('<div.*?author clearfix">.*?<h2.*?>(.*?)</h2>.*?<div.*?'+
                                 'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items=re.findall(pattern,data)
        pageStories=[]
        for item in items:
            #需要排除有图片的内容
            haveImg=re.search("img",item[3])
            #需要将时间戳改成正常时间
            item2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(item[2])))
            #如果不含图片，把它加入list中
            if not haveImg:
                replaceBr=re.compile('</br>')
                text=re.sub(replaceBr,'\n',item[1])
                #item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
                pageStories.append([item[0].strip(),text.strip(),item2,item[4]])
        return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if self.enable==True:
            if len(self.stories) < 2:
                pageStories=self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            inp=input()
            self.loadPage()
            if inp=='q':
                self.enable=False
                return 
            print(u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s"%(page,story[0],story[2],story[3],story[1]))

    def start(self):
        print(u'正在读取糗事百科,按回车查看新段子，q退出')
        self.enable=True
        self.loadPage()
        nowPage=0
        while self.enable:
            if len(self.stories)>0:
                pageStories=self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

if __name__ == '__main__':
    spider=QSBk()
    spider.start()