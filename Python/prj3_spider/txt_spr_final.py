#!/usr/bin/python
#coding=utf-8

import urllib,urllib2
import re
import sys

def getPage(page_num=1):
    url='https://www.qiushibaike.com/8hr/page/'+str(page_num)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
        return html
    except urllib2.URLError,e:
        if hasattr(e,"code"):
            print "连接服务器失败，错误代码%s"%e.code
            return None
        if hasattr(e,"reason"):
            print "连接服务器失败，错误原因%s"%e.reason
            return None

def getPageContent(page_num=1):
    html=getPage(page_num)
#    print html
#    re_page=re.compile(r'<div class="author.*?>.*?<a.*?<img.*?alt="(.*?)">.*?<div class="content"><span>(.*?)</span></div>.*?<div class="stats">.*?<i class="number">(\d+)</i>',re.S)
#    re_page=re.compile(r'<div class="author.*?>.*?<a.*?<img.*?alt="(.*?)">.*?<div class="content">.*?<span>(.*?)</span>.*?</div>.*?<div class="stats">.*?<i class="number">(\d+)</i>',re.S)
    re_page=re.compile(r'<div class="author.*?>.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>.*?<div class="stats">.*?<i class="number">(\d+)</i>',re.S)
    items=re_page.findall(html)
    page_contents=[]
    replaceBR1=re.compile(r'<br/>')
    replaceBR2=re.compile(r'<span></span>')
    for item in items:
        new_content=replaceBR1.sub('\n',item[1])
        page_contents.append([page_num,
                            item[0].strip(),
                            new_content.strip(),
                            item[2].strip()])
    return page_contents

def getOneStory(page_contents):
    for story in page_contents:
        input=raw_input()
        if input== 'Q' or input=='q':
            sys.exit()
        print "第%d页\t发布人:%s\n%s\n赞:%s\n"%(story[0],story[1],story[2],story[3])

if __name__=='__main__':
    print "正在读取段子，按回车看新段子，退出（Q|q）"
    num=1
    while True:
        page_contents=getPageContent(num)
        getOneStory(page_contents)
        num+=1
    
