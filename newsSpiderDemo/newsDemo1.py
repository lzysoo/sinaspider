# coding='utf-8'

import requests
from bs4 import BeautifulSoup
import datetime


#newsurl = 'http://news.sina.com.cn/china/'
newsurl = 'https://news.sina.com.cn/zx/2019-01-21/doc-ihqfskcn9221513.shtml'
res = requests.get(newsurl)
res.encoding = 'utf-8'
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
#抓取新闻标题 class = main-title
title = soup.select('.main-title')[0].text
#抓取新闻时间
timesource = soup.select('.date')[0].text
#字符串转换为时间类型
dt = datetime.datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')
#获取新闻来源 class = source
source = soup.select('.source')[0].text
#获取新闻内容 id = article
content = soup.select('#article p')[:-1]
#将内容合并到一个list
article = []
for p in content:
    article.append(p.text.strip())
#以'/'连接每一个段落
#'/'.join(article)

print(title + '\t' + newsurl + '\t' + str(dt) + '\t' + str(article) + '\n')