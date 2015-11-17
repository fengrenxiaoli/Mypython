#/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib
import urllib.request
import re

'''
Tool类是为了处理BDTB类获取数据中的多余标签
'''

#处理页面标签类
class Tool:
    #去除img标签，7位长空格
    removeImg=re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr=re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD=re.compile('<td>')
    #将段落开头换为\n加空两格
    replacePara=re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR=re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtratag=re.compile('<.*?>')
    def replace(self,x):
        x=re.sub(self.removeImg,'',x)
        x=re.sub(self.removeAddr,'',x)
        x=re.sub(self.replaceLine,'\n',x)
        x=re.sub(self.replaceTD,'\t',x)
        x=re.sub(self.replacePara,'\n',x)
        x=re.sub(self.replaceBR,'\n',x)
        x=re.sub(self.removeExtratag,'',x)
        #strip()将前后多余内容删除
        return x.strip()

'''
BDTB类定义了获取帖子某一页的内容、获取帖子的标题、获取帖子的页数以及将导出的文本文件命名为帖子标题的方法、写入帖子正文的方法，还有main()
可以继续写，比如整理某个贴吧所有的精品贴，再利用这个文件的类和方法
标题和页数，每一页的帖子都可以获得
'''

#百度贴吧爬虫类
class BDTB:
    #初始化，传入基地类，是否只看楼主的参数
    def __init__(self,baseurl,seelz,floorTag):
        #base链接地址
        self.baseurl=baseurl
        #是否只看楼主
        self.seelz='?see_lz='+str(seelz)
        #html标签剔除工具类对象
        self.tool=Tool()
        #楼层标号，初始为1
        self.file=None
        #默认的标号，初始为1
        self.floor=1
        #默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle=u'百度贴吧'
        #是否写入楼分隔符的标记
        self.floorTag=floorTag

    #传入页码，获取该页帖子的代码
    def getPage(self,pagenum):
        try:
            url=self.baseurl+self.seelz+'&pn='+str(pagenum)
            request=urllib.request.Request(url)
            reponse=urllib.request.urlopen(request)
            #print(reponse.read().decode('utf-8'))
            return reponse.read().decode('utf-8')
        #无法链接，报错
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print(u'连接百度贴吧失败,错误原因',e.reason)
                return None
                
    #获取帖子标题
    def getTitle(self,page):
        #得到标题的正则表达式
        pattern=re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result=re.search(pattern,page)
        if result:
            #如果存在，则返回数值
            return result.group(1).strip()
        else:
            #因为发现存在h3的标题==
            pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
            result=re.search(pattern,page)
            if result:
                return result.group(1).strip()
            else:
                return None
        
    #获取帖子一共有多少页
    def getpagenum(self,page):
        #获取帖子页数的正则表达式
        pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result=re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取每一层楼的内容，传入页面内容
    def getcontent(self,page):
        #匹配所有楼层的内容
        pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items=re.findall(pattern,page)
        contents=[]
        for item in items:
            # with open('baidutieba.txt','a') as f:
            #     f.write(item)
            # print('\n\n',floor,u' 楼------------------------------------------------------------------------------------')
            # print(self.tool.replace(item))
            # floor+=1
            #将文本进行去除标签处理，同时在前后加入换行符
            content='\n'+self.tool.replace(item)+'\n'
            contents.append(content.encode('utf-8'))
        return contents

    def setfiletitle(self,title):
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file=open(title+'.txt','w+')
        else:
            self.file=open(self.defaultTitle+'.txt','w+')

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            if self.floorTag=='1':
                #楼之间的分隔符
                floorLine='\n'+str(self.floor)+u' 楼---------------------------------------------------------------'
                self.file.write(floorLine)
            self.file.write(str(item,encoding='utf-8'))
            # self.file.write(item)
            self.floor+=1

    def main(self):
        indexPage=self.getPage(1)
        pageNum=self.getpagenum(indexPage)
        title=self.getTitle(indexPage)
        self.setfiletitle(title)
        if pageNum==None:
            print('URL已失效，请重试')
            return None
        try:
            print('该帖子共有'+str(pageNum)+'页')
            self.file.write(baseurl)
            for i in range(1,int(pageNum)+1):
                print('正在写入第'+str(i)+'页数据')
                page=self.getPage(i)
                contents=self.getcontent(page)
                self.writeData(contents)
        #出现写入异常
        except IOError as e:
            print('写入异常，原因是'+e.message)
        finally:
            print('写入任务完成')

if __name__ == '__main__':
    print('请输入帖子代号:')
    baseurl='http://tieba.baidu.com/p/'+str(input('http://tieba.baidu.com/p/'))
    seelz=input('是否只获取楼主发言，是输入1，否输入0\n')
    floorTag=input('是否写入楼层信息，是输入1，否输入0\n')
    bdtb=BDTB(baseurl, seelz, floorTag)
    bdtb.main()
