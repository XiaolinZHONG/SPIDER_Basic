#coding=utf-8
import re
import urllib
import urllib2
import time
import thread


removeImg=re.compile('<img.*?>| {7}')
removeAddr=re.compile('<a.*?>|</a>')
replaceLine=re.compile('<tr>|<div>|</div>|</p>')
replaceTD=re.compile('<td>')
replacePara=re.compile('<p.*?>')
replaceBR=re.compile('<br><br>|<br>')
removeExtraTag=re.compile('<.*?>')
def replace(x):
    x=re.sub(removeImg," ",x)
    x=re.sub(removeAddr," ",x)
    x=re.sub(replaceLine,"\n",x)
    x=re.sub(replaceTD,"\t",x)
    x=re.sub(replacePara,"\n     ",x)
    x=re.sub(replaceBR,"\n",x)
    x=re.sub(removeExtraTag," ",x)
    return x.strip()


user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}
url='http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read().decode('utf-8')
except urllib2.URLError,e:
    if hasattr(e,'reason'):
        print u'连接失败的原因',e.reason
        
patternone=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
resultone=re.search(patternone,html)
#注意这里使用的是search不是findall
if resultone:
    print resultone.group(1).strip()
    #这里必须使用的是group（1），如果不填写数值会整个正则表达式的内容全部显示出来

patterntwo=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
resulttwo=re.search(patterntwo,html)
#这里使用的也是search
if resulttwo:
    print resulttwo.group(1).strip()

patternthree=re.compile('<div id="post_content.*?>(.*?)</div>',re.S)
items=re.findall(patternthree,html)
floor=1
for item in items:
    print floor,u'level----------------\n'
    print replace(item)
    floor+=1
