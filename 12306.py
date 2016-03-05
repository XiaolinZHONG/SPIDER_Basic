#coding=utf-8

import re
from time import sleep
import os
from splinter.browser import Browser
initmy_url='https://kyfw.12306.cn/otn/index/initMy12306'
ticket_url='https://kyfw.12306.cn/otn/leftTicket/init'
b=Browser(driver_name='chrome') #模拟chrome浏览器登录
b.visit(ticket_url)#需要打开的网页

#b.fill('wd','splinter')#通过chrome的F12可以看到输入框的name=wd,fill的内容是splinter
#button=b.find_by_value(u'百度一下')#百度搜索栏的value=”百度一下”,id=”su”
#button=b.find_by_id(u'su')
#button.click()#模拟点击百度一下
#if b.is_text_present('splinter.cobrateam.info'):
#    print  'True'
#else:
#    b.quit()
username=u'xlzhong123@163.com'
passwd=u'020002118_'
zz=u'%u67A3%u5E84%2CZEK'
sh=u'%u4E0A%u6D77%2CSHH'
dtime=u'2016-02-14'
order=0
passenger=u'钟啸林'
b.find_by_text(u'登录').click()#这里的by text和前面的by value,by id差不多
sleep(3)
b.fill("loginUserDTO.user_name",username)
b.fill("userDTO.password",passwd)#这里需要通过F12来寻找<input中的name对应的
print u'wait for you to input the 验证码....'
while True:
    if b.url!=initmy_url:
        sleep(1)
    else:
        break

print(u'跳回购票页面....')
b.visit(ticket_url)
b.cookies.add({'_jc_save_fromStation':zz})
b.cookies.add({'_jc_save_toStation':sh})
b.cookies.add({'_jc_save_fromDate':dtime})
b.reload()
sleep(2)

count=0
if order!=0:
    while b.url==ticket_url:
        b.find_by_text(u'查询').click()
        count+=1
        print u'正在尝试第%s次' %count
        sleep(0.5)
        try:
            b.find_by_text(u'预订').click()
        except:
            print u'还没开始预定'
            continue
else:
    while b.url==ticket_url:
        b.find_by_text(u'查询').click()
        sleep(1)
        b.find_by_text(u'GC-高铁/城际').click()
        b.find_by_text(u'D-动车').click()
        sleep(1)
        count+=1
        print u'正在尝试第%s次' %count
        sleep(1)
        try:
            for i in b.find_by_text(u'预订'):
                i.click()
        except:
            print u'还没开始预定'
            continue