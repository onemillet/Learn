#!/usr/bin/python
#coding=utf-8

import urllib,urllib2
import re

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
    re_page=re.compile(r'<div class="author.*?>.*?<a.*?<img.*?alt="(.*?)">.*?<div class="content">.*?<span>(.*?)</span>.*?</div>.*?<div class="stats">.*?<i class="number">(\d+)</i>',re.S)
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

if __name__=='__main__':
    page_contents=getPageContent()
    for item in page_contents:
        for i in item:
            print i
        print '================='
