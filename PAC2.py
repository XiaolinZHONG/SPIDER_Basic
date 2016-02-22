#coding=utf-8
import re
email=r"\w{3}@w+(\.com|\.cn)"
emailer=r".+?@.+?\.com|\.cn" #正确的邮箱正则
#emailer=r".+?@.+?(\.com|\.cn)" #优先返回括号里的东西
print re.findall(email,'zzz@csvt.com')
print re.findall(emailer,'zzz@csvt.com')

s='''hhsdj dskj hello src=cavt yes
jdjsds djhsjk src=123 yes
jdsa src=234 yes
hello src=python yes  ksa'''
r1=r"hello src=.+ yes"
print re.findall(r1,s)
r2=r"hello src=(.+) yes"
print re.findall(r2,s)
