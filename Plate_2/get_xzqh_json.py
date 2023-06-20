'''
author:Chenxu Zhang
date:2023.06.19
description:这个板块获得的是用于制作作者粉丝的热力地图以及性别统计图
'''
import requests
from bs4 import BeautifulSoup
import csv
import json

#这个函数不需要多次使用，只需要在开始时获得json文件即可，用于解码爬取到的用户
def get_loccodes():
    # 中华人民共和国行政区划代码
    url = 'https://www.mca.gov.cn/mzsj/xzqh/2022/202201xzqh.html'
    locs = {}
    try:
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = "utf-8"
            soup = BeautifulSoup(r.text, 'html5lib')
            items = soup.find_all('tr', attrs={"height": "19"})
            # 城市编码的个数
            print(print(len(items)))
            for item in items:
                # 提取数据
                locs[item.find_all('td')[1].text] = item.find_all('td')[2].text.replace("\xa0\xa0 ","")
                locs[item.find_all('td')[1].text] = locs[item.find_all('td')[1].text].strip("\xa0")
    except:
        print("获取失败！")
    json_data = json.dumps(locs)
    with open('Plate_2/data/xzqh.json', 'w') as file:
        file.write(json_data)

#获取作者粉丝的信息，只获取粉丝的性别和ip地址
def get_fan_inf(url):
    r = requests.get(url)
    soup = r.json()
    data_loc = []
    data_gender = []
    try:
        fans = soup['data']
        for fan in fans:
            data_loc.append(fan['userProfile']['city'])
            data_gender.append(fan['userProfile']['gender'])
    except:
        pass
    return data_gender,data_loc        
        
#一个用来计数的函数
def count_elements(lst):
    counts = {}  
    for element in lst:
        if element in counts:
            counts[element] += 1  
        else:
            counts[element] = 1 
    return counts

#一个用来修改地理位置数据格式的函数，主要是为了html接收
def loc_tool(dict_loc):
    new_dict = []
    with open('Plate_2/data/xzqh.json', 'r') as file:
        json_data = json.load(file)
        data_check = dict(json_data)
    for key, value in dict_loc.items():
        if str(key) in data_check:
            new_key = data_check[str(key)].replace("\xa0","")
            new_value = value
            new_dict.append({'name':new_key,'value':new_value})
    return new_dict        

#控制主函数，循环爬取作者的所有粉丝的信息
def main(artist_id):
    offsets = [0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
    data_loc_all = []
    data_gender_all = []
    for offset in offsets:
        url = f"http://localhost:3000/artist/fans?id={artist_id}&limit=500&offset={offset}"
        print(url)
        data_gender,data_loc = get_fan_inf(url)
        data_gender_all.extend(data_gender)
        data_loc_all.extend(data_loc)
    #以下内容用来控制数据格式调整
    dict_loc = count_elements(data_loc_all)
    dict_gender = count_elements(data_gender_all)
    new_loc = loc_tool(dict_loc)
    new_gender = {}
    for key,value in dict_gender.items():
        if key == 2:
            new_gender['female'] = value
        if key == 1:
            new_gender['male'] = value
        if key == 0:
            new_gender['unknow'] = value
    return new_loc,new_gender

#这里用于筛选有效的城市编码信息并将其和爬取的数据结合
def generate_new_dictionary():
    new_dict = {}
    with open('Plate_2/data/data.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    for item in data:
        if item['city'] == '市辖区' and item['area'] != '':
            new_key = item['area']
        elif item['area'] == '' and item['city'] != '市辖区':
            new_key = item['city']
        else:
            continue
        #构造储存经纬度信息
        new_value = [item['lng'], item['lat']]
        new_dict[new_key] = new_value
    return new_dict
