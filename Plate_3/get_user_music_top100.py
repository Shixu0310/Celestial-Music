'''
author:Chenxu Zhang
date:2023.06.19
description:获取用户最喜爱的音乐top100
'''
import requests
from bs4 import BeautifulSoup
import csv

# 构造函数获取用户前100听歌记录
def get_top100(url,user_id):
    r = requests.get(url)
    soup = r.json()
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    try:
        with open(filename, 'a', encoding='utf-8-sig', newline='') as csvfile:    # 文件存储的位置
            writer = csv.writer(csvfile)
            for song in soup['allData']:
                song_id = song['song']['id']
                song_name = song['song']['name']
                play_count = song['playCount']
                artist_name = song['song']['ar'][0]['name']
                artist_id = song['song']['ar'][0]['id']
                try:
                    writer.writerow((song_id,song_name,play_count,artist_name,artist_id))
                except Exception as msg:
                    print(msg)
    except:
        pass

#主控制函数
def main(user_id):
    type_data = 0
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('song_id','song_name','play_count','artist_name','artist_id'))
    #获取地址
    url = 'http://localhost:3000/user/record?uid=' + str(user_id) + '&type=' + str(type_data)
        #开始获取数据
    print('enter:',url)
    get_top100(url,user_id)

