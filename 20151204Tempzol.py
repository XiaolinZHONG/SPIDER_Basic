# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import os
import time
from BeautifulSoup import BeautifulSoup, Tag

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://detail.zol.com.cn/405/404011/param.shtml'
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('gbk')
    
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason
#print html

#pattern=u'<a href="(/\d.*?)".*?更多参数>></a>.*?</li>.*?</ul>'
#items=re.findall(pattern,html)
#print items

soup=BeautifulSoup(html)
print soup.find('title').getText()
print soup.find(attra={'var proName ='})
#print soup.find('head')
#print soup.head
#print soup.contents[0]
#print soup.contents[1]
#print soup.contents[2]
#get title
pattern=u'<h1.*?>(.*?)参数.*?</h1>'
title=re.search(pattern,html)
#print title
print title.group(1).strip()

#get frame
patternsheet=re.compile('<table>.*?<th>(.*?)</th>.*?</table>',re.S)
itemsheet=re.findall(patternsheet,html)
print len(itemsheet)
print itemsheet[0]
print itemsheet[1]
print itemsheet[2]
print itemsheet[3]
print itemsheet[4]
print itemsheet[5]
print itemsheet[6]
print itemsheet[7]
print itemsheet[8]
print itemsheet[9]
print itemsheet[10]
#get frame
patternsheet=re.compile('<table>(.*?)</table>',re.S)
itemsheet=re.findall(patternsheet,html)
#print itemsheet[0]
#print itemsheet[1]
#print itemsheet[2]
#print itemsheet[3]
#print itemsheet[4]
#print itemsheet[5]

#get time
patternone=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
itemsone=re.findall(patternone,itemsheet[0])

for itemone in itemsone:
    havehref=re.search('a href.*?',itemone[1])
    print u'------------\n'
    print itemone[0]
    if havehref:
        newitemone=re.findall('<a href=.*?>(.*?)</a>',itemone[1])
        for new in newitemone:
            print new
    else:
        print itemone[1]
