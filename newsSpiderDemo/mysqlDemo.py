import pymysql
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456',db='crawler')
cur = conn.cursor()
cur.execute("SELECT * FROM huxiu_news_spider")
#result = cur.fetchall()
#for r in result:
 #   print(r)
#print(result)
data = pd.DataFrame(list(cur.fetchall()))
cur.close()
conn.close()

print(data.shape)
print(data.info())
print(any(data.duplicated()))
print(any(data.isnull()))
data_rownull = data.shape[0] - data.count()
#print(data_rownull)
data_rownull = data.shape[1] - data.count(axis=1)
#print(data_rownull)
'''

connect = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
print('yes')
data = pd.DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('xyzw'))
data.to_sql('test1',connect,schema='test',if_exists='append',index=False,index_label=False)
#pd.io.sql.to_sql(data, 'test1', connect, schema='test', if_exists='append',index=False,index_label=False)
'''