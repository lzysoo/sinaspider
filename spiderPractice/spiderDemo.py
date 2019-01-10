#新浪新闻爬虫

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.sina.com.cn/china/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text ,'html.parser')
news = soup.select('.right-content')[0]
right = news.select('a[href]')
for ele in right :
    print(ele.text)
print("===============================================")
switch_text = soup.select('.switch-text')[0]
switch = switch_text.select('a[href]')
for ele in switch :
    print(ele.text)
print("===============================================")

#有一段新闻标题不知如何打印，找不到对应的class
#btn_box = soup.select()[0]
#btn = btn_box.select('a[href]')
#for ele in btn :
#   print(ele.text)


