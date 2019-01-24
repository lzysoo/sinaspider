import random
import urllib
import re
import json


#设置服务器代理
def get_one_page(my_headers,url):
    randdom_header = random.choice(my_headers)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", randdom_header)
    req.add_header("GET", url)
    response = urllib.request.urlopen(req)
    return  response
#代理服务器
my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]

#获取原网页
def get_href(html):
    pattern = re.compile('<div class="mod-b mod-art clearfix "'
                         '.*?"transition"  href="(.*?)"'
                         '.*?</div>', re.S)
    items =re.findall(pattern, html)
    return items

#使用正则表达式，解析原网页
def parse_one_page(href):
    pattern = re.compile('<div class="article-wrap">'
                         '.*?class="t-h1">(.*?)</h1>'
                         '.*?article-time pull-left">(.*?)</span>'
                         '.*?article-share pull-left">(.*?)</span>'
                         '.*?article-pl pull-left">(.*?)</span>'
                       #  '.*?text-remarks.*?</p><p><br/></p><p>(.*?)<!--.*?认证-->'
                         '.*?author-name.*?<a href=".*?" target="_blank">(.*?)</a>'
                         '.*?author-one">(.*?)</div>'
                         '.*?author-article-pl.*?target="_blank">(.*?)</a></li>'
                         '.*?</div>', re.S)

    #将获得的参数值转化成键值对
    items =re.findall(pattern, href)
    for item in items:
        yield {
            'title': item[0].strip(),
            'time': item[1],
            'share': item[2][2:],
            'recoment': item[3][2:],
            #   'content': re.compile(r'<[^>]+>',re.S).sub('',item[4]).strip(),
            'anthor': item[4].strip(),
            'intro': item[5],
            'passNum': item[6]
        }

def write_to_file(content):
    with open('text.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

for i in range(len(url_html)):
    url_ord = "https://www.huxiu.com" + url_html[i]
    ord_text = get_one_page(my_headers, url_ord).read().decode('utf-8')
    for item in parse_one_page(ord_text):
        print(item)
        write_to_file(item)

