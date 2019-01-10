#coding:utf8
import re
import string
import sys
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests
from lxml import etree

user_id = 1230663070
cookie = {"Cookie" : "_T_WM=5eedb753b36b1133094a2fc3345be784; WEIBOCN_FROM=1110006030; SUB=_2A25xN2NADeRhGeBH6VIZ-C_KyjWIHXVS2A0IrDV6PUJbkdAKLWGgkW1NQdsQWmJDZc7dQUVc6VVjl5mfGGrnGFPI; SUHB=00xZn6LPboGI_7; SCF=AmYMcc5SNVYQmLimKPr09Kqai5nMKx27iQaEeJHqBdD2Q5DUVIn_HegGX5--I60e8uHiSZrHdEhWxwORnv9rVN4.; SSOLoginState=1546851088; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D1076031230663070%26luicode%3D20000174%26uicode%3D20000174"}

url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id
html = requests.get(url,cookies = cookie,verify = False).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name = "mp"]')[0].attrib['value'])

print(pageNum)   #88

result = ""
urllist_set = set()
word_count = 1
image_count = 1
for page in range(1,2) :
    #获取lxml页面
    url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page)
    lxml = requests.get(url,cookies = cookie,verify = False).content
    #文字爬取
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content :
        text = each.xpath('string(.)')
        if word_count >= 4 :
            text = "%d :"%(word_count - 3) + text + "\r\n"
        else :
            text = text + "\r\n"
        result = result + text
        word_count += 1
    '''
    #图片爬去
    soup = BeautifulSoup(lxml,"lxml")
    urllist = soup.find_all('a',href = re.compile(r"^https://weibo.cn/mblog/oripic",re.I))
    first = 0
    for imgurl in urllist :
        urllist_set.add(requests.get(imgurl['href'],cookies = cookie).url)
        image_count += 1
        #print(urllist_set)
    '''
#打印出前4页的微博内容
#print(result)
fo1 = open("E:/software/JetBrains/%s_TYan.txt"%user_id,"wb")
fo1.write(bytes(result,'UTF-8'))
fo1.close()

'''
#将爬取的图片的url地址保存下来
link = ""
fo2 = open("E:/software/JetBrains/%s_TangY.txt"%user_id,"wb")
for eachlink in urllist_set :
    link = link + "\n" + eachlink
fo2.write(bytes(link,'UTF-8'))
fo2.close()
print("图片链接爬取完毕")


#将爬取的图片下载保存本地
if not urllist_set :
    print("该页面中不存在图片")
else :
    #
    image_path = 'E:/software/JetBrains'+'/weibo_image'
    print(image_path)
    if os.path.exists(image_path) is False :
        os.mkdir(image_path)
    x = 1
    for imgurl in urllist_set :
        temp = image_path + '/%s.jpg' % x
        print('正在下载第%s张图片' % x)
        try :
            urllib.request.urlretrieve(imgurl,temp)
        except:
            print('该图片下载失败：%s' % imgurl)
        x += 1
#print('原创微博爬取完毕，共%d条，保存路径%s'%(word_count - 4,word_path))
#print('微博图片爬取完毕，共%d条，保存路径%s'%(image_count - 1,image_path))
'''