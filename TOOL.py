#coding=utf-8
import re

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
    x=re.sub(removeLine,"\n",x)
    x=re.sub(replaceTD,"\t",x)
    x=re.sub(replacePara,"\n     ",x)
    x=re.sub(replaceBR,"\n",x)
    x=resub(replaceExtraTag," ",x)
    return x.strip()


