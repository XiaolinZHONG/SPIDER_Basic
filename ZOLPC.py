#coding=utf-8

import re
import urllib
import urllib2
import time
import thread
import os

f=open('d:\Project\zolpc.txt','w+')
def getdetailhtml(html):
    pattern=u'<li>.*?<a href="(/\d.*?)".*?target=.*?>更多参数.*?</a>.*?</li>'
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
    pattern=u'<h1.*?>(.*?)参数.*?</h1>'
    title=re.search(pattern,html)
    f.write(u'\n--------------\n')
    f.write( u'电脑名称'.encode('utf-8'))
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
        havehref=re.search('a href.*?',itemone[1])
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
        havehref=re.search('a href.*?',itemtwo[1])
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
        havehref=re.search('a href.*?',itemfour[1])
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
            havehref=re.search('a href.*?',itemfive[1])
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
            havehref=re.search('a href.*?',itemsix[1])
            f.write(u'\n--------------\n')
            f.write(itemsix[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemsix[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemsix[1].encode('utf-8'))
    #getI/O
    if 7<=maxsheet-1:
        patternseven=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
        itemsseven=re.findall(patternseven,itemsheet[7])
        for itemseven in itemsseven:
            havehref=re.search('a href.*?',itemseven[1])
            f.write(u'\n--------------\n')
            f.write(itemseven[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemseven[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemseven[1].encode('utf-8'))
    #getinput
    if 8<=maxsheet-1:
        patterneight=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
        itemseight=re.findall(patterneight,itemsheet[8])
        for itemeight in itemseight:
            havehref=re.search('a href.*?',itemeight[1])
            f.write(u'\n--------------\n')
            f.write(itemeight[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemeight[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemeight[1].encode('utf-8'))

    if 9<=maxsheet-1:
        patternnine=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
        itemsnine=re.findall(patternnine,itemsheet[9])
        for itemnine in itemsnine:
            havehref=re.search('a href.*?',itemnine[1])
            f.write(u'\n--------------\n')
            f.write(itemnine[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemnine[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemnine[1].encode('utf-8'))

    if 10<=maxsheet-1:
        patternten=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
        itemsten=re.findall(patternten,itemsheet[10])
        for itemten in itemsten:
            havehref=re.search('a href.*?',itemten[1])
            f.write(u'\n--------------\n')
            f.write(itemten[0].encode('utf-8'))
            f.write('\n')
            if havehref:
                newitemone=re.findall('<a href=.*?>(.*?)</a>',itemten[1])
                for new in newitemone:
                    f.write(new.encode('utf-8'))
            else:
                f.write(itemten[1].encode('utf-8'))


user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
count=1

#使用range的时候应该大一位数值
for i in range(1,156):
    pagenum=i
    url='http://detail.zol.com.cn/notebook_advSearch/subcate16_1_s6316-s6133-s5719-s5364-s4998_1_1__'+str(pagenum)+'.html#showc'
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('gbk')
    for item in getdetailhtml(html):
        print u'\n*******************\n                ',count,u'\n*******************\n'
        getinfo(item)
        count+=1

f.close()
