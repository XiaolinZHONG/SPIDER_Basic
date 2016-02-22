# coding=utf-8
import re
import urllib
import urllib2

values={}
values['username']="xlzhong123@163.com"
values['password']="020002118"

loginurl="http://www.zhihu.com/#signin"
topicurl="http://www.zhihu.com/topic"

data=urllib.urlencode(values) #由字典转化为字符串

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
referer={'Referer':'http://www.zhihu.com/topic'}
#若访问的次数过多会被禁止访问这个时候可以设置代理服务器来实现
#import urllib2
#enable_proxy = True
#proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
#null_proxy_handler = urllib2.ProxyHandler({})
#if enable_proxy:
#    opener = urllib2.build_opener(proxy_handler)
#else:
#    opener = urllib2.build_opener(null_proxy_handler)
#urllib2.install_opener(opener)

#request=urllib2.Request(url,data,headers,referer)
request=urllib2.Request(url,data,headers)
respone=urllib2.urlopen(request,timeout=10) #等待10秒钟就超时
print respone.read()

