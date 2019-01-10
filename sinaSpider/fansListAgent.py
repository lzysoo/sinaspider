#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
    Create by Kobe On 2019.1.8 00:02
    说明：抓取m站粉丝列表
"""
import random
import time
import urllib.request

import json
import codecs

fansListFile = codecs.open('fansList.txt', 'a', 'utf-8')
def crawlDetailPage(url, pageId, browser):
    global fansListFile

    # 读取m站微博网页的 json 信息
    headers = ('User-Agent', browser)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    jsondata = opener.open(url).read()
    data = json.loads(bytes(jsondata).decode('utf-8'))

    # 判断本页是否有内容
    # {'ok': 0, 'data': {'msg': '这里还没有内容', 'ok': 0, 'title': '粉丝', 'cardlistInfo': {'containerid': '1005051654024040_-_FANS', 'page': 14, 'title': None}}}
    if '这里还没有内容' == data['data']['msg']:
        return data             # 此处必须返回 data，否则调用方法时，if条件句会出错

    # 获取本页每一条数据
    content = data['data']['cards']
    for fans in content:
        user = fans['user']
        line = str(user_oid) + '\t' + str(user)
        fansListFile.write(line + '\r\n')
    return data

user_oid = 1005051654024040
pageId = 0
pageIds = []
count = 0
browsers = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4763.400',
              'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
              'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
              'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'
              ]

# 浏览器的列表生成式
def traversal_list(alist, i):
    while True:
        length = len(alist)
        i = i % length
        yield alist[i]
        i += 1

while count <= 10:
    print('正在获取第{}页的粉丝列表'.format(pageId))
    url = 'https://m.weibo.cn/api/container/getSecond?containerid={user_oid}_-_FANS&page={pageId}'.format(user_oid=user_oid, pageId=pageId)
    # 无限循环浏览器列表
    browser = next(traversal_list(browsers, pageId))
    data = crawlDetailPage(url, pageId, browser)

    if '这里还没有内容' == data['data']['msg']:
        pageIds.append(pageId)
        if len(pageIds) >= 10:
            for i in range(1, len(pageIds)):
                if pageIds[i] - pageIds[i - 1]:
                    count += 1

    pageId = pageId + 1

    # 设置休眠时间
    t = random.randint(2, 3)
    print('休眠时间：{}s'.format(t))
    time.sleep(t)



