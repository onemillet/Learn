#!/usr/bin/env python

import urllib, urllib2
import re

def getHtml(url):
    page=urllib2.urlopen(url)
    return page.read()

def getImage(html):
    re_img=re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')
    img_list=re_img.findall(html)
#    return img_list
    i=1
    for img_url in img_list:
        print img_url
        urllib.urlretrieve(img_url,filename="%s.jpg"%i)
        i+=1

if __name__=="__main__":
    url='http://tieba.baidu.com/p/4229162765'
    page=getHtml(url)
    img=getImage(page)
#    print img

