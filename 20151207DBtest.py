#coding=utf-8

import re
import urllib2
import urllib
import os
import time
import BeautifulSoup

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
pagenum=10
count=1
#for pagnum in range(10,7220):
url='http://movie.douban.com/subject/25964071/'
#    pagnum+=20

try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read()
    
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason

soup=BeautifulSoup.BeautifulSoup(html)
#print soup.find('title').getText()
item=soup.find(attrs={'class':'subjectwrap clearfix'})
#为什么使用的是class为item，是因为后面的部分全部是以这个为分割的

#print items

#for item in items:
    #print u'\n****************',count,u'****************\n'
pic=item.find(attrs={'class':'subject clearfix'})
    #inte=item.find(attrs={'id':'interest_sectl'})
    #print pic
    #print pic['href'] #详细信息网址
    #print pic['title']
    #print pic['src']
    #print pic.img['src'] #获得图片网址
    #print pic.img['alt'] #这一句实际上是可以执行的
    #get the acttrs
    #actor=pic.find(attrs={'class':'actor'})
    #print actor.find(attrs={'class':'pl'}).getText()
    #attrs=actor.findAll(attrs={'rel':'v:starring'})
    #for attr in attrs:
    #    print attr
#get the style

info=pic.find(attrs={'id':'info'})
styles=info.findAll(attrs={'class':'pl'})
for st in styles:
    print st.getText()

#get
    #print info
    #print info.a.getText()
    #print info.p.getText()
    #print info.a.getText().replace(' ','')
    #print info.a.getText().replace('\n','')
    #print info.a.getText().replace(' ','').replace('\n','')#1
    #x=info.a.getText().replace(' ','').replace('\n','')
    #print re.sub('[\t]+','',x)#2 和#1中的效果一样，实际上re.sub的功能就是替换可以参考前面的抓取百度贴吧的程序
    #get评分部分
    #star=info.find(attrs={'class':'star clearfix'})#bs对层次的要求比较高，需要每一层每一层的剥离出来，后面会验证需不需要
    #print获得的得分
    #print star.find(attrs={'class':'rating_nums'}).getText()
    #print 评论人数
    #print star.find(attrs={'class':'pl'}).getText().replace('(','').replace(')','')#一般情况下一个括号（）要分两部分才能完全替换掉
    #count+=1

