#coding=utf-8
import re
import urllib
import urllib2
import time
import thread

#QSBKspider
class QS:

    #定义变量及函数,由于是面向对象的函数，所以应该使用的变量是self和作为的_int_来编写
    #这一段是专门用来编写面向对象编程的定义语句
    def _init_(self):
        self.page=raw_input('pls input you want to go:')
        #这样写可能会失败
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
        self.headers={'User-Agent':user_agent}
        self.stories=[]
        #存储
        self.enable=False
        #存放是否运行变量

    #想要获取的页面
    def gethtml(self,page):
        try:
            url='http://www.qiushibaike.com/hot/page/1'
            request=urllib2.Request(url,headers=headers)
            #这个地方的headers只能用这种格式
            response=urllib2.urlopen(request)
            html=response.read().decode('utf-8')
            #这一句也非常重要，因为默认的编码可能不是中文
            return html
            #因为定义函数了，所以一定要有返回值
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print "连接失败的原因", e.reason
            #一个非常有用的打印方法
    def gethtml(self,page):
        html=gethtml(self,page)
        
        pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items=re.findall(pattern,html)
        
