# coding=utf-8

import re
import urllib
import urllib2
import time
import thread

pagenum=2
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://detail.zol.com.cn/369/368499/param.shtml'
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('gbk')
    #可以通过浏览器查看网页的编码方式为什么，一般常见的有GBK UTF-8 UNICODE这几种
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason
#print html
#get title
pattern=u'<title>【(.*?)参数.*?</title>'
title=re.findall(pattern,html)
print title[0]

#get CPU
patterntwo=u'<span id.*?>CPU频率</span>.*?<span id="newPmVal_18">.*?<a href=.*?>.*?</a>'
frequ=re.findall(patterntwo,html)
print frequ
   


