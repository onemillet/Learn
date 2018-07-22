#!/usr/bin/pyghon
#coding:utf-8

import urllib,urllib2
import re
import cookielib

class MyCpy(object):
    def __init__(self):
        self.headers={'User-Agent':''}
        self.baseURL=''
        self.loginURL=self.baseURL+''
    
    def getPage(self):
        self.cookie=cookielib.CookieJar()
        handler=urllib2.HTTPCookieProcessor(self.cookie)
        self.opener=urllib2.build_opener(handler)
        try:
            request=urllib2.Request(url=self.baseURL,headers=self.headers)
#            response=urllib2.urlopen(request)
            response=self.opener.open(request)
            return response.read()
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print "连接服务器失败，错误原因：%s"%e.reason
                return None
    
    def getTocken(self):
        page=self.getPage()
        re_tocken=re.compile(r'',re.S)
        tocken=re.tocken.search(page)
        if tocken:
            print tocken.group(1)
            return tocken.group(1)
        else:
            return None

    def login(self):
        data={"_tocken":self.getTocken(),
            "_task":"",
            "_action":"",
            "_timezone":"Asia/Shanghai",
            "_url":"",
            "_user":"",
            "_pass":""}
        self.postdata=urllib.urlencode(data)
        try:
            request=urllib2.Request(url=self.loginURL,
                                    data=self.postdata,
                                    headers=self.headers)
#           response=urllib2.urlopen(request)
            response=self.opener.open(request)
            response.read()
            print response.read()
        except urllib2.URLError,e:
            print e

gpy=MyCpy()
gpy.getTocken()
gpy.login()
