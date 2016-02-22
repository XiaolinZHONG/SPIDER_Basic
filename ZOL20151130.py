#coding=utf-8

import re
import urllib
import urllib2
import time
import thread
import os

f=open('d:\Project\zol1415.txt','w+')
def getdetailhtml(html):
    pattern=u'<a href="(.*?)".*?>更多参数.*?</a>'
    items=re.findall(pattern,html)
    return items
    

def getinfo(detailhtml):
    user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
    headers={'User-Agent':user_agent}
    url='http://detail.zol.com.cn'+str(detailhtml)
    try:
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read().decode('gbk')
    except urllib2.URLError,e:
        if hasattr(e,'reason'):
            print u'连接失败的原因',e.reason
    #gettitle
    pattern=u'<title>【(.*?)参数.*?</title>'
    title=re.search(pattern,html)
    f.write(u'\n--------------\n')
    f.write( u'手机名称'.encode('utf-8'))
    f.write('\n')
    f.write(title.group(1).strip().encode('utf-8'))
    #return title.group(1).strip()
    #getframe
    patternsheet=re.compile('<table>(.*?)</table>',re.S)
    itemsheet=re.findall(patternsheet,html)
    maxsheet=len(itemsheet)
    print maxsheet
    #print itemsheet[1]
    #gettime
    patternone=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
    itemsone=re.findall(patternone,itemsheet[0])
    for itemone in itemsone:
        havehref=re.search('a href.%?',itemone[1])
        f.write(u'\n--------------\n')
        f.write(itemone[0].encode('utf-8'))
        f.write('\n')
        if havehref:
            newitemone=re.findall('<a href=.*?>(.*?)</a>',itemone[1])
            for new in newitemone:
                f.write(new.encode('utf-8'))
        else:
            f.write(itemone[1].encode('utf-8'))
    #return itemsone
    #getscreen
    patterntwo=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
    itemstwo=re.findall(patterntwo,itemsheet[1])
    for itemtwo in itemstwo:
        havehref=re.search('a href.%?',itemtwo[1])
        f.write(u'\n--------------\n')
        f.write(itemtwo[0].encode('utf-8'))
        f.write('\n')
        if havehref:
            newitemone=re.findall('<a href=.*?>(.*?)</a>',itemtwo[1])
            for new in newitemone:
                f.write(new.encode('utf-8'))
        else:
            f.write(itemtwo[1].encode('utf-8'))
        
    #gethardware
    patterntwo=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
    itemsfour=re.findall(patterntwo,itemsheet[4])
    for itemfour in itemsfour:
        havehref=re.search('a href.%?',itemfour[1])
        f.write(u'\n--------------\n')
        f.write(itemfour[0].encode('utf-8'))
        f.write('\n')
        if havehref:
            newitemone=re.findall('<a href=.*?>(.*?)</a>',itemfour[1])
            for new in newitemone:
                f.write(new.encode('utf-8'))
        else:
            f.write(itemfour[1].encode('utf-8'))
    #return itemsfour
    #getcamera
    if 5<=maxsheet-1:
        patternfive=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
        itemsfive=re.findall(patternfive,itemsheet[5])
        for itemfive in itemsfive:
            havehref=re.search('a href.%?',itemfive[1])
            f.write(u'\n--------------\n')
            f.write(itemfive[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemfive[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemfive[1].encode('utf-8'))
    
    #getappearance
    if 6<=maxsheet-1:
        patternsix=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
        itemssix=re.findall(patternsix,itemsheet[6])
        for itemsix in itemssix:
            havehref=re.search('a href.%?',itemsix[1])
            f.write(u'\n--------------\n')
            f.write(itemsix[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemsix[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemsix[1].encode('utf-8'))


user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
count=1

#使用range的时候应该大一位数值
for i in range(1,61):
    pagenum=i
    url='http://detail.zol.com.cn/cell_phone_advSearch/subcate57_1_s6132-s5359_1_1_0_'+str(pagenum)+'.html#showc'
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('gbk')
    for item in getdetailhtml(html):
        print u'\n*******************\n                ',count,u'\n*******************\n'
        getinfo(item)
        count+=1

f.close()
