# coding=utf-8

import re
import urllib
import urllib2
import time
import thread


user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://detail.zol.com.cn/403/402591/param.shtml'
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('gbk')
    
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason
#print html
        
#get title
pattern=u'<title>【(.*?)参数.*?</title>'
title=re.search(pattern,html)
print title.group(1).strip()

#get frame
patternsheet=re.compile('<table>.*?<th>(.*?)</th>.*?</table>',re.S)
itemsheet=re.findall(patternsheet,html)
print itemsheet[0]
print itemsheet[1]
print itemsheet[2]
print itemsheet[3]
print itemsheet[4]
print itemsheet[5]

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

#get frame
#patterntwo=re.compile('<table>.*?<th>(.*?)</th>.*?</table>',re.S)
#items=re.findall(patterntwo,html)
#for item in items:
#    print u'--------------\n'
#    print item
    
#print items[0]
#print items[1]
#print items[3]
#print items[4]

#get frame2
#patternsheet=re.compile('<div class="param-.*?>.*?<ul class.*?>(.*?)</ul>.*?</div>',re.S)
#itemsheet=re.findall(patternsheet,html)
#print itemsheet[4]

#getframe3

#gettime
#patternone=re.compile('<li>.*?<span id=.*?>(.*?)</span>.*?<a href=.*?>(.*?)</a>.*?</span>.*?</li>',re.S)
#itemsone=re.findall(patternone,itemsheet[1])
#patternfour2=re.compile('<li>.*?<span id=.*?>.*?<a href=.*?>(.*?)</a>.*?</span>.*?</li>',re.S)
#itemsfour2=re.findall(patternfour2,itemsheet[1])
#for itemone in itemsone:
#    print u'--------------\n'
#    print itemone[0]
#    print itemone[1]
#print itemsfour2[0]
#如何并排显示？


#gethardware
#patternfour=re.compile('<li.*?>.*?<span id=.*?>(.*?)</span>.*?<a href=.*?>(.*?)</a>.*?</span>.*?</li>',re.S)
#itemsfour=re.findall(patternfour,itemsheet[4])
#patternfive2=re.compile('<li>.*?<span id=.*?>.*?<a href=.*?>(.*?)</a>.*?</span>.*?</li>',re.S)
#itemsfive2=re.findall(patternfive2,itemsheet[4])
#for itemfour in itemsfour:
#   print u'--------------\n'
#   print itemfour[0]
#   print itemfour[1]
    
#for itemfive2 in itemsfive2:
#    print itemfive2


#getcamera
#patternfive=re.compile('<li.*?>.*?<span id=.*?>(.*?)</span>.*?<a href=.*?>(.*?)</a>.*?</span>.*?</li>',re.S)
#itemsfive=re.findall(patternfive,itemsheet[5])
#for itemfive in itemsfive:
#   print u'--------------\n'
#   print itemfive[0]
#   print itemfive[1]

#getappearance
#patternsix=re.compile('<li.*?>.*?<span id=.*?>(.*?)</span>.*?<span id=.*?>(.*?)</span>.*?</li>',re.S)
#itemssix=re.findall(patternsix,itemsheet[6])
#for itemsix in itemssix:
#    havehref=re.search('a href.*?',itemsix[1])
#    if not havehref:
#        print u'--------------\n'
#        print itemsix[0]
#        print itemsix[1]
