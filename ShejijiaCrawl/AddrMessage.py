# coding:utf-8

# 引入相关模块
import requests
import json
import os

#写入文件路径
path='F:\\addrMessage\\addr.txt'
#判断该路径下是否有该文件，有则删除文件
if os.path.exists(path):
    os.remove(path)

# 地址信息链接
url="https://fpmw.shejijia.com/api/rest/v1.0/tenant/ezhome/asset/templates/addresses"
# 请求地址信息的URL，获取其text文本
addrData = requests.get(url).text
#加载为json格式数据
data=json.loads(addrData)
#获取到‘items’对应的值
newData=data["items"]
sum=0
#遍历各区域，获取片区相关值
for n in newData:
    zone=n["name"]
    countByZone=n["count"]
    child1=n["children"]
    #遍历各省份，获取省份相关值
    for child2 in child1:
        provinceId=child2["id"]
        privinceName=child2["name"]
        child3=child2["children"]
        #遍历各城市，获取城市相关值
        for child4 in child3:
            cityId=child4["id"]
            cityName=child4["name"]
            countByCity=child4["count"]
            sum+=countByCity
            print(provinceId,cityId,privinceName,cityName,countByCity)
            #打开文件，写入数据
            file = open(path,'a')
            file.write(provinceId+'\t'+cityId+'\t'+privinceName+'\t'+cityName+'\t'+str(countByCity)+'\n')
print(sum)
file.close()