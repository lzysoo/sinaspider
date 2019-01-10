#网易新闻标题

import requests
from bs4 import BeautifulSoup

#模拟chrome浏览器
url= "http://news.163.com/domestic/"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
res = requests.get(url,headers = headers)
#res.encoding = 'gbk'
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text,'html.parser')

#爬取到的新闻标题乱码,网易使用的是GBK编码，所以开始时出现中文乱码
today_news = soup.select(".today_news")[0]
today_title = today_news.select('a[href]')
for ele in today_title :
    print(ele.text)
print("===========================================")
second_news = soup.select(".second_right")[0]
second_title = second_news.select('a[href]')
for ele in second_title :
    print(ele.text)
