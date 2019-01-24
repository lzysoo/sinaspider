# -*- coding: utf-8 -*-

import urllib.request
import json
import random
import sinaTweetsSpider.Proxies
import sinaTweetsSpider.UserAgent
import time
from lxml import etree

#定义要爬取的微博大V的微博ID
#id='1219847813'
#id='1230663070'
id = '3945647785'

#设置代理IP
#proxy_addr="122.241.72.191:808"
#proxy_addr = sinaTweetsSpider.Proxies.proxies

#定义页面打开函数
#def use_proxy(url,proxy_addr):
def use_proxy(url):
    req=urllib.request.Request(url)
    ie = random.choice(sinaTweetsSpider.UserAgent.pcUserAgent)
    proxy = random.choice(sinaTweetsSpider.Proxies.proxies)
    #req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    req.add_header("User-Agent",ie)
    #proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    proxy_handler = urllib.request.ProxyHandler(proxy)
    #opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
    return data

#获取微博主页的containerid，爬取微博内容时需要此id
def get_containerid(url):
    #data=use_proxy(url,proxy_addr)
    data = use_proxy(url)
    content=json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if(data.get('tab_type')=='weibo'):
            containerid=data.get('containerid')
    return containerid
print(get_containerid('https://m.weibo.cn/api/container/getIndex?type=uid&value=1230663070'))

#获取微博大V账号的用户基本信息，如：微博昵称、微博地址、微博头像、关注人数、粉丝数、性别、等级等
def get_userInfo(id):
    url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
    #data=use_proxy(url,proxy_addr)
    data = use_proxy(url)
    content=json.loads(data).get('data')
    profile_image_url=content.get('userInfo').get('profile_image_url')
    description=content.get('userInfo').get('description')
    profile_url=content.get('userInfo').get('profile_url')
    verified=content.get('userInfo').get('verified')
    guanzhu=content.get('userInfo').get('follow_count')
    name=content.get('userInfo').get('screen_name')
    fensi=content.get('userInfo').get('followers_count')
    gender=content.get('userInfo').get('gender')
    urank=content.get('userInfo').get('urank')
    print("微博昵称："+name+"\n"+"微博主页地址："+profile_url+"\n"+"微博头像地址："+profile_image_url+"\n"+"是否认证："+str(verified)+"\n"+"微博说明："+description+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+gender+"\n"+"微博等级："+str(urank)+"\n")
    with open('sina.txt','a',encoding = 'utf-8') as userInfo:
        userInfo.write(id + "\t" + name+ "\t" + profile_url + "\t" + str(verified) + "\t" + description + "\t" + str(guanzhu) + "\t" +str(fensi) + "\t" + gender + "\t" + str(urank) + "\n")

#判断日期是否符合格式,不符合直接添加(当年发的微博没有年份，所以需要判断一下)
def is_valid_date(str_date):
    try:
       time.strptime(str_date,"%Y-%m-%d")
       return True
    except:
       return False

def add_year_date(str_date):
    if(is_valid_date(str_date)):
        str_date = str_date
    else:
        str_date = '2019-'+str_date
    return str_date

#获取微博内容信息,并保存到文本中，内容包括：每条微博的内容、微博详情页面地址、点赞数、评论数、转发数等
'''
def get_weibo(id,file):
    i=1
    while True:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            data=use_proxy(weibo_url,proxy_addr)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(len(cards)>0):
                for j in range(len(cards)):
                    print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
                    card_type=cards[j].get('card_type')
                    if(card_type==9):
                        mblog=cards[j].get('mblog')
                        attitudes_count=mblog.get('attitudes_count')
                        comments_count=mblog.get('comments_count')
                        created_at=mblog.get('created_at')
                        reposts_count=mblog.get('reposts_count')
                        scheme=cards[j].get('scheme')
                        text=mblog.get('text')
                        with open(file,'a',encoding='utf-8') as fh:
                            fh.write("----第"+str(i)+"页，第"+str(j)+"条微博----"+"\n")
                            fh.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(add_year_date(created_at))+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")
                i+=1
            else:
                break
        except Exception as e:
            print(e)
            pass
'''
#判断日期是否在指定时间范围内
def is_target_date(str_date,start_date):
    cur_array = time.strptime(str_date,"%Y-%m-%d")
    cur_stamp = time.mktime(cur_array)
    start_array = time.strptime(start_date,"%Y-%m-%d")
    start_stamp = time.mktime(start_array)
    return cur_stamp >= start_stamp

def get_weibo(id,file):
    i=1
    while True:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            #data=use_proxy(weibo_url,proxy_addr)
            data = use_proxy(weibo_url)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(len(cards)>0):
                for j in range(len(cards)):
                    print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
                    card_type=cards[j].get('card_type')
                    if(card_type==9):
                        mblog = cards[j].get('mblog')
                        created_at = mblog.get('created_at')
                        new_created_at = add_year_date(created_at)
                        #判断时间是否在2019-01-01之后，是则爬取，否则停止
                        if(is_target_date(new_created_at,'2018-01-01')):
                            attitudes_count=mblog.get('attitudes_count')
                            comments_count=mblog.get('comments_count')
                            reposts_count=mblog.get('reposts_count')
                            scheme=cards[j].get('scheme')
                            text=mblog.get('text')
                            #text = text.decode("utf-8")
                            '''pattern = re.compile(u'[\u4E00-\u9FA5]+')
                            new_text = pattern.findall(text)
                            print("text:"+new_text)'''
                            text_html = etree.HTML(text) #将text转换为HTML格式
                            new_text = text_html.xpath('string(.)')
                            #print("text:" + new_text)
                            with open(file,'a',encoding='utf-8') as fh:
                                #fh.write("----第"+str(i)+"页，第"+str(j)+"条微博----"+"\n")
                                #fh.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(new_created_at)+"\n"+"微博内容："+new_text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")
                                fh.write(id + "\t" + str(scheme) + "\t" + str(new_created_at) + "\t" + new_text + "\t" + str(attitudes_count) + "\t" + str(comments_count) + "\t" + str(reposts_count) + "\n")

                        else:
                            return
                i+=1
            else:
                break
        except Exception as e:
            print(e)
            pass

if __name__=="__main__":
    file=id+".txt"
    get_userInfo(id)
    get_weibo(id,file)