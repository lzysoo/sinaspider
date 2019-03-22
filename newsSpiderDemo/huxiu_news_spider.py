from pyspider.libs.base_handler import *
import json
from pyquery import PyQuery as pq
import numpy as np
import pandas as pd
import pymysql
import time
from sqlalchemy import create_engine

#db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456',db='news',charset='utf8')
#cursor = db.cursor()
connect = create_engine("mysql+pymysql://root:123456@localhost:3306/crawler?charset=utf8")

class Handler(BaseHandler):
    crawl_config ={
        "headers":{
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'X-Requested-With':'XMLHTTPRequest'
        }
    }

    def get_taskid(self, task):
        return md5string(task['url']+json.dumps(task['fetch'].get('data','')))

    @every(minutes=24 * 60)
    def on_start(self):
        for page in range(2,3):
            #print('正在爬去第%s页' % page)
            self.crawl('https://www.huxiu.com/v2_action/article_list',method='POST',data={'page':page},callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        content = response.json['data']
        doc = pq(content)
        lis = doc('.mod-art').items()
        data = [{
            'title':item('.msubstr-row2').text(),
            'url':'https://www.huxiu.com'+str(item('.msubstr-row2').attr('href')),
            'name':item('.author-name').text(), #开始爬取到的name字段都为空，因为代码刚开始author-name前丢了 .
            'write_time':item('.time').text(),
            'comment':item('.icon-cmt+ em').text(),
            'favorites':item('.icon-fvr+ em').text(),
            'abstract':item('.mob-sub').text(),
            'tag':item('column-link').text()
        }for item in lis]
        #print(data)
        return data
        #for each in response.doc('a[href^="http"]').items():
            #self.crawl(each.attr.href, callback=self.detail_page)

    '''@config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }'''

    def on_result(self, result):
        if result:
            self.save_to_mysql(result)

    def save_to_mysql(self,result):
        df = pd.DataFrame(result)
        #content = json.loads(df.T.to_json()).values()
        pd.io.sql.to_sql(df, 'huxiu_news', connect, schema='crawler', if_exists='append')
        #if connect.insert(content):
            #print('存储到MySQL成功')
        sleep = np.random.randint(1,5)
        time.sleep(sleep)


