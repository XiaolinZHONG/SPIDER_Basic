#coding=utf-8
import re
import urllib
import urllib2
import time
import thread


#I PART 请求

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_0-1000_0_1_1_0_1.html'

try:
    request=urllib2.Request(url,headers=headers)
    #这个地方的headers只能用这种格式
    response=urllib2.urlopen(request)
    html=response.read()
    
except urllib2.URLError, e:
    if hasattr(e,"reason"):
        print u"连接失败的原因", e.reason
        #一个非常有用的打印方法

#II PART 抓取

pattern=re.compile('<div class=.*?>.*?<a href=.*?>(.*?)</a>.*?<ul class="param clearfix">(.*?)</ul>',re.S)
items=re.findall(pattern,html)

for item in items:
    print item[0]
    print item[1]
