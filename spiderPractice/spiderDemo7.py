#start_chrome --> input-date --> scroll_down --> find_cards_info -->save -->find_next
#爬取指定时间内的微博
# （还有bug）

from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def start_chrome():
    #driver = webdriver.Chrome(executable_path='./chromedriver')
    driver  = webdriver.Chrome()
    #打开chrome客户端
    driver.start_client()
    return driver

def q(st,et):
    return '?is_ori=1&key_word=&start_time={st}&end_time={et}&is_search=1&is_searchadv=1#_0'

def scroll_down():
    #定位页面
    html_page = driver.find_element_by_tag_name('html')
    for i in range(15):
        print(i)
        #模拟发送END按键（网页滑到底）
        html_page.send_keys(Keys.END)
        #间隔时间0.6秒
        time.sleep(0.6)

def find_cards_info():
    #单条微博区块，CSS路径
    cards_sel = 'div.WB_feed_detail'
    #定位到单条微博区块
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []
    for card in cards:
        content_sel = 'div.WB_text.W_f14'
        time_sel = 'div.WB_from.S_txt2'
        link_sel = 'div.WB_from.S_txt2>a:nth-child(1)'

        content = card.find_element_by_css_selector(content_sel).text
        time = card.find_element_by_css_selector(time_sel).text
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        info_list.append([content,time,link])
    # int_sel = 'span>span.line.S_line1>span>em:nth-child(2)'
    #
    # most = driver.find_elements_by_css_selector(int_sel)
    # rep,comm,like = [str(el.text) for el in most[1:]]
    # print(most)
    # print(rep)


    return info_list

def find_next():
    next_sel = 'a.page.next'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')

def save(info_list,name):
    full_path = './'+name + '.csv'
    #如果当前目录下已有该名字的文件，则在该文件中添加数据；没有则重新创建并添加数据
    if os.path.exists(full_path):
        with open(full_path,'a',newline='',encoding='utf-8') as f :
            writer = csv.writer(f)
            writer.writerows(info_list)
            print('Done!')
    else:
        with open(full_path,'w+',newline='',encoding='utf-8') as f :
            writer = csv.writer(f)
            writer.writerows(info_list)
            print('Done!!')

def run_crawler(base,duration ):
    if not base.endswith('feedtop'):
        st,et = duration.split('~')
        #第一个为开始时间，第二个为结束时间
        driver.get(base+q(st,et))
    else:
        driver.get(base)
    time.sleep(5)
    scroll_down()
    time.sleep(5)
    info_list = find_cards_info()
    save(info_list,duration)
    next_page = find_next()
    if next_page:
        run_crawler(next_page,duration)

#个人微博主页
base = 'https://weibo.com/p/1005055793083716'
driver = start_chrome()
input()
#时间可替换
run_crawler(base,'2017-04-20~2018-08-10')
