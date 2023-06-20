'''
author:Chenxu Zhang
date:2023.06.19
description:此处获得用户的基本信息，同时可以检查用户id填写是否正确
'''
import requests
from bs4 import BeautifulSoup
import csv

#获取用户的基本信息
def get_inf(url):
    gender_dic = {0:'unknow',1:'male',2:'female'}
    r = requests.get(url)
    soup = r.json()
    inf = soup['profile']
    name = inf['nickname']
    signature = inf['signature']
    imgurl = inf['avatarUrl']
    gender = gender_dic[inf['gender']]
    viptype = inf['vipType']
    return name,signature,imgurl,gender,viptype

#获取最热门歌曲的名字
def get_hotest(url):
    r = requests.get(url)
    soup = r.json()
    try:
        hot = soup['weekData'][0]['song']['name']
    except:
        hot = "Haven't listened to any songs recently"
    return hot

#主函数
def main(user_id):
    url = 'http://localhost:3000/user/detail?uid=' + str(user_id) 
    name,signature,imgurl,gender,viptype = get_inf(url)
    url2 = 'http://localhost:3000/user/record?uid=' + str(user_id) + '&type=1'
    hotest = get_hotest(url2)   
    #返回获取的信息
    return name,signature,imgurl,gender,viptype,hotest
