#coding:utf-8

import requests
import json
import os

url = "https://news.sina.com.cn/china/"
newsData = requests.get(url).text
print(newsData)
data = json.loads(newsData)
print(data)