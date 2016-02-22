#coding=utf-8

import re
import urllib
import urllib2
import os
import time
from BeautifulSoup import BeautifulSoup, Tag

#removeImg=re.compile('<img.*?>| {7}')
#removeAddr=re.compile('<a.*?>|</a>')
#replaceLine=re.compile('<tr>|<div>|</div>|</p>')
#replaceTD=re.compile('<td>')
#replacePara=re.compile('<p.*?>')
#replaceBR=re.compile('<br><br>|<br>')
removeExtraTag=re.compile('<.*?>')
def replace(x):
    #x=re.sub(removeImg," ",x)
    #x=re.sub(removeAddr," ",x)
    #x=re.sub(replaceLine,"\n",x)
    #x=re.sub(replaceTD,"\t",x)
    #x=re.sub(replacePara,"\n     ",x)
    #x=re.sub(replaceBR,"\n",x)
    x=re.sub(removeExtraTag,"",x) #注意这个地方是没有空格的，专门用来紧凑整个结果
    return x.strip()

def readhtml(url):
    user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
    headers={'User-Agent':user_agent}
    try:
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
    except urllib2.URLError,e:
        if hasattr(e,'reason'):
            print u'连接失败的原因',e.reason
    return html




count=1
f=open('d:\Project\DBDYxjtop.txt','w+')
pagenum=0
for pagenum in range(0,362):
    url='http://movie.douban.com/tag/%E5%96%9C%E5%89%A7?start='+str(pagenum*20)+'&type=T'
    html=readhtml(url)
    soup=BeautifulSoup(html)
    print soup.find('title').getText()
    items=soup.findAll(attrs={'class':'item'})
     #为什么使用的是class为item，是因为后面的部分全部是以这个为分割的
    for item in items:
        print u'\n********',count,u'*********\n'
        pic=item.find(attrs={'class':'nbg'})
        f.write(u'\n------------------\n')
        f.write(pic['title'].encode('utf-8'))
        detail=str(pic['href'])
        
        htmld=readhtml(detail)
        
        soupd=BeautifulSoup(htmld)
        itemd=soupd.find(attrs={'class':'subjectwrap clearfix'})
        picd=itemd.find(attrs={'class':'subject clearfix'})
        infoone=picd.find(attrs={'id':'info'})
        infotwo=replace(str(infoone))
        f.write(u'\n')
        f.write(infotwo)
        star=item.find(attrs={'class':'star clearfix'})
        f.write(u'\n')
        f.write( u'评分:'.encode('utf-8'))
        f.write(star.find(attrs={'class':'rating_nums'}).getText().encode('utf-8'))
        f.write(u'\n')
        comnum=star.find(attrs={'class':'pl'}).getText().replace('(','').replace(')','')
        f.write(comnum.encode('utf-8'))
        f.write(u'\n')
        count+=1

f.close()
        
        
        
            
        
