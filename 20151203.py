#coding=utf-8

import re
import urllib
import urllib2
import time
import xml.sax
import os

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) '
headers={'User-Agent':user_agent}

class DYTT:
    url='https://www.dytt8.net'
    try:
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
    except urllib2.URLError,e:
        if hasattr(e,'reason'):
            print u'the reason why you can\'t connect to the web',e.reason

    def startElement(self,tag,attributes):
        CurrentData=tag
