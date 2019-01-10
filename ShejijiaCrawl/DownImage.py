# coding:utf-8

import json
import os
import time
import urllib.request


def get_img(url,new_file):
    conn=urllib.request.urlopen(url)
    name='D:image'+new_file[9:-4]+'.png'
    if not os.path.exists(name[:-40]):
        os.makedirs(name[:-40])
    f=open(name,'wb')
    f.write(conn.read())
    f.close()
    os.remove(new_file)
    print("Down finished!!!")


def json_analyze(wbdata,new_file):
    for fi in wbdata:
        try:
            data=json.loads(fi)
            url=data["meta"]["backgroundimage"]["url"]
            get_img(url,new_file)
        except:
            print('there are not fond url')
            continue

def gci(filepath):
    count=0
    files=os.listdir(filepath)
    for fi in files:
        fi_d=os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            count+=1
            new_file=os.path.join(filepath,fi_d)
            print(count,new_file)
            word=open(new_file,'r',encoding='utf-8').readlines()
            json_analyze(word,new_file)
            time.sleep(0.1)

filepath='F:\\forImg\\河南'
gci(filepath)
