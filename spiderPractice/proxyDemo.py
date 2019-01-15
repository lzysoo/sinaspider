#coding:utf-8

#使用代理的三种方法

import requests
import urllib.request
import random

#使用requests

#proxy = '1223.241.116.247:18118'
proxies = {
    'http': 'http://122.241.72.191:808',
    'https': 'https://223.241.119.183:18118'
}
try:
    response = requests.get('http://www.baidu.com', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

#使用urllib

