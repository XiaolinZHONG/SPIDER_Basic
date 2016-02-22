#coding=utf-8
import re
import urllib
import urllib2
import time
import thread


#I PART 请求

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://www.qiushibaike.com/hot/page/1'

try:
    request=urllib2.Request(url,headers=headers)
    #这个地方的headers只能用这种格式
    response=urllib2.urlopen(request)
    html=response.read().decode('utf-8')
    
except urllib2.URLError, e:
    if hasattr(e,"reason"):
        print u"连接失败的原因", e.reason
        #一个非常有用的打印方法

#II PART 抓取

pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
#通过chrome浏览器得到的代码注意：即使是换行也应该用.*？来表示，注意为什么不用.+?
items = re.findall(pattern,html)

for item in items:
    print item[0]
    print item[1]
    print item[2]
    print item[3]
    print item[4]
   
