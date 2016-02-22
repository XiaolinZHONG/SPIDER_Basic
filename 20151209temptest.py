# -*- coding: utf-8 -*-
import re
import urllib2
import urllib
import os
import time
from BeautifulSoup import BeautifulSoup,Tag

removeImg=re.compile('<img.*?>| {7}')
removeAddr=re.compile('<a.*?>|</a>')
replaceLine=re.compile('<tr>|<div>|</div>|</p>')
replaceTD=re.compile('<td>')
replacePara=re.compile('<p.*?>')
replaceBR=re.compile('<br><br>|<br>')
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




user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://movie.douban.com/subject/25964071/'


try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read()
    
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason

soup=BeautifulSoup(html)
item=soup.find(attrs={'class':'subjectwrap clearfix'})
pic=item.find(attrs={'class':'subject clearfix'})
info=pic.find(attrs={'id':'info'})
#print info

#removeIIX=re.compile('<.*?>')
#info=removeIIX.sub('',str(info))
#print info.strip()
print replace(str(info))
i#ntere1=soup.find(attrs={'class':'rating_wrap clearbox'})
#intere2=soup.find(attrs={'class':'rating_self clearfix'})
#new=replace(str(intere2))
#remove=re.compile('\n')
#info=remove.sub(' ',new)
#print u'豆瓣评分:',info.strip()
