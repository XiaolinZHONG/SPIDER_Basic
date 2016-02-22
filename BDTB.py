# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
class BDTB:
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        #base链接地址
        self.baseURL = baseUrl
        #是否只看楼主
        self.seeLZ = '?see_lz='+str(seeLZ)
        #HTML标签剔除工具类对象
        self.tool = Tool()
        #全局file变量，文件写入操作对象
        self.file = None
        #楼层标号，初始为1
        self.floor = 1
        #默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"百度贴吧"
        #是否写入楼分隔符的标记
        self.floorTag = floorTag
 
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            #构建URL
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #返回UTF-8格式编码内容
            return response.read().decode('utf-8')
        #无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None
 
    #获取帖子标题
    def getTitle(self,page):
        #得到标题的正则表达式
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            #如果存在，则返回标题
            return result.group(1).strip()
        else:
            return None
 
    #获取帖子一共有多少页
    def getPageNum(self,page):
        #获取帖子页数的正则表达式
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
 
    #获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        #匹配所有楼层的内容
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            #将文本进行去除标签处理，同时在前后加入换行符
            content = "\n"+self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents

baseURL='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL,1)

