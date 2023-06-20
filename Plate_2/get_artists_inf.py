'''
author:Chenxu Zhang
date:2023.06.19
description:获得作者的基本信息
'''
import requests
from bs4 import BeautifulSoup
import csv

#获取作者基本信息
def get_inf(url):
    r = requests.get(url)
    soup = r.json()
    inf = soup['data']['artist']
    img_url = inf['avatar']
    name = inf['name']
    briefdesc = inf['briefDesc'].replace('\n', '')
    try:
        back_url = soup['data']['user']['backgroundUrl']
        user_id = soup['data']['user']['userId']
    except:
        back_url = "static/picture/backurl.png" 
        user_id =  "None"
    data_list = []
    all = 0
    for item in soup['data']['secondaryExpertIdentiy']:
        data_list.append({'name': item['expertIdentiyName'],'value': item['expertIdentiyCount']})
        all += item['expertIdentiyCount']
    return img_url,name,briefdesc,back_url,user_id,data_list,all


#主控函数，没啥特别的，不如去翻垃圾桶（^.^）
def main(artist_id):
    url = 'http://localhost:3000/artist/detail?id=' + str(artist_id) 
    img_url,name,briefdesc,back_url,user_id,data_list,all = get_inf(url)
    data_list = sorted(data_list, key=lambda x: x['value'], reverse=True)
    if len(briefdesc) > 150:
        briefdesc = briefdesc[:150] + "..."
    data_inf = [img_url,name,briefdesc,back_url,user_id]
    return data_inf,data_list,all
