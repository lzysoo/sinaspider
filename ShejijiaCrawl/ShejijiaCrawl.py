# coding:utf-8

import json
import os
import random
import shutil
import time
import socket

import requests
import requests.packages

#import main.python.fjn.shejijia.Proxies
#import main.python.fjn.shejijia.UserAgent

import ShejijiaCrawl.Proxies
import ShejijiaCrawl.UserAgent


def get_pictureDetail(assetId,houseTypePathSub):

    sid="publicdesign"
    id=assetId
    versionId="undefined"

    url="https://fpmw.shejijia.com/api/rest/v1.0/design?sid="+sid+"&id="+id+"&versionId="+versionId

    # NET_STATUS=False
    # while not NET_STATUS:
    #     try:
    #         wbdata = requests.get(url, proxies=ShejijiaCrawl.Proxies.proxies,timeout=3).text
    #     except socket.timeout:
    #         print('NET_STATUS is not good')
    #         NET_STATUS=False
    wbdata = requests.get(url, proxies=ShejijiaCrawl.Proxies.proxies,verify=False).text
    # data=json.loads(wbdata)
    houseTypePath=houseTypePathSub+assetId+'.txt'
    houseTypeFile=open(houseTypePath,'w',encoding='utf-8')
    houseTypeFile.write(wbdata)
    houseTypeFile.flush()
    # print(wbdata)
    # print(data["meta"]["image2d"]["url"])
    # data1=json.loads(data["data"])
    # data2=data1["data"]


def get_assetId(cityId,countByCity,assertIdPath,houseTypePathSub):
    times=57618
    startOffset=57618
    slidLenth=9
    while(startOffset<=int(countByCity)):
        #随机获取一个常用的浏览器
        ie=random.choice(ShejijiaCrawl.UserAgent.pcUserAgent)
        print(ie)
        #请求头
        headers={
            'Host':'fpmw.shejijia.com',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':'gzip, deflate, br',
            'Content-Type':'application/json',
            'Referer':'https://3d.shejijia.com/',
            'Content-length':'148',
            'Origin':'https://3d.shejijia.com',
            'Connection':'close',
            'User-Agent':ie
        }
        #请求参数
        format={'attributes':['cityId_'+cityId],'fieldsToStat':['neighborName'],'offset':startOffset,'limit':slidLenth,'sortField':'TimeCreated','sortOrder':'desc'}
        s=json.dumps(format)
        #发送post请求
        req=requests.post(url, data=s, headers=headers, proxies=ShejijiaCrawl.Proxies.proxies,verify=False)
        da=json.loads(req.text)
        li=da["items"]
        for l in li:
            times=times+1
            assetId=l["id"]
            assetIdFile=open(assertIdPath,'a')
            assetIdFile.write('NO'+str(times)+'\t'+assetId+'\n')
            assetIdFile.flush()
            print('NO'+str(times)+'\t'+assetId)
            get_pictureDetail(assetId,houseTypePathSub)

        startOffset+=slidLenth
        #随机睡眠一段时间
        time.sleep(random.random())


#搜索框的请求链接
url='https://fpmw.shejijia.com/api/rest/v1.0/tenant/ezhome/asset/templates/search'
#地址信息的文件路径
addrPath='F:\\addrMessagePart\\addr.txt'
assertIdDir='F:\\assertMessage\\'
houseTypeDir='F:\\houseTypeMessage\\'
#判断该路径下是否有该文件，有则删除文件
# if os.path.exists(assertIdDir):
#     shutil.rmtree(assertIdDir)
# if os.path.exists(houseTypeDir):
#     shutil.rmtree(houseTypeDir)

#读取文件
f=open(addrPath,'r')
lines=f.readlines()
#对文件进行遍历
for line in lines:
    words=line.split('\t')
    #获取相应的数据
    provinceId=words[0]
    cityId=words[1]
    provinceName=words[2]
    cityName=words[3]
    countByCity=words[4]
    if not os.path.exists(assertIdDir+provinceName):
        os.makedirs(assertIdDir+provinceName)
    assertIdPath=assertIdDir+provinceName+'\\'+cityName+'.txt'
    if not os.path.exists(houseTypeDir+provinceName+'\\'+cityName):
        os.makedirs(houseTypeDir+provinceName+'\\'+cityName)
    houseTypePathSub=houseTypeDir+provinceName+'\\'+cityName+'\\'
    get_assetId(cityId,countByCity,assertIdPath,houseTypePathSub)



