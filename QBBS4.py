#coding=utf-8
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='https://en.wikipedia.org/wiki/Xi_Jinping'
try:
    request=urllib2.Request(url,headers=headers)
    #这个地方的headers只能用这种格式
    response=urllib2.urlopen(request)
    html=response.read().decode('utf-8')
    
except urllib2.URLError, e:
    if hasattr(e,"reason"):
        print u"连接失败的原因", e.reason
soup=BeautifulSoup(response)
soup.title.string
