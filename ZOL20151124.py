#coding=utf-8

import re
import urllib
import urllib2
import time
import thread

pagenum=2
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://detail.zol.com.cn/cell_phone_advSearch/subcate57_1_s5329_1_1__'+str(pagenum)+'.html#showc'
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('gbk')
    #可以通过浏览器查看网页的编码方式为什么，一般常见的有GBK UTF-8 UNICODE这几种
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason


#patternone=re.compile('<dl class=.*?>.*?<dt>.*?<a href=.*?>(.*?)</a>',re.S)
#itemsone=re.findall(patternone,html)
#count=1
#for itemone in itemsone:
#    print count,u'-----------\n'
#    print itemone
#    count+=1
#gethtml
pattern=u'<a href="(.*?)".*?>更多参数.*?</a>'
items=re.findall(pattern,html)
count=1
for item in items:
    print count,u'-----------\n'
    print str(item)
    count+=1

#print str(items[0])
#print itemsone[0]

#patterntwo=re.compile('<li title=.*?>(网络类型.*?)</li>',re.S)
#itemstwo=re.findall(patterntwo,html)
#for itemtwo in itemstwo:
#    print itemtwo

#patterntwo=u'<li title=.*?>(CPU型号.*?)</li>'
#itemstwo=re.findall(patterntwo,html)
#itemtwo=itemstwo[0]
#type(itemstwo)
#count=1
#for itemtwo in itemstwo:
#    print count,u'-----------\n'
#    print itemtwo
  
    
