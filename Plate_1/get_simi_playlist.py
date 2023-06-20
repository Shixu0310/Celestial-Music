'''
author:Chenxu Zhang
date:2023.06.19
description:这里是获得歌单推荐的板块
'''
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# 构造函数获取用户推荐的歌单
def get_simi_music(url,user_id):
    r = requests.get(url)
    soup = r.json()
    filename1 = f"Plate_1/data/simi_playlist/simi_playlist_{user_id}.csv"
    try:
        playlists = soup['playlists']
    except:
        return
    with open(filename1, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        for playlist in playlists:
            try:
                list_id = playlist['id']
                list_name = playlist['name']
                list_url = playlist['coverImgUrl']
                list_tag = ','.join(playlist['tags'])
                list_des = playlist['description'].replace("\n","")
                if len(list_des) > 50:
                    list_des = list_des[:50] + "..."
                writer.writerow((list_id,list_name,list_url,list_tag,list_des))
            except:
                continue
            
#读取csv的小工具    
def read_csv_column(csv_file, column_name):
    data = []
    with open(csv_file, 'r',encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                data.append(row[column_name])
    return data

#主要操作函数，顺便去重
def main(user_id):
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    list_ids = read_csv_column(filename, 'song_id')
    filename1 = f"Plate_1/data/simi_playlist/simi_playlist_{user_id}.csv"
    with open(filename1, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('list_id','list_name','list_url','list_tag','list_des'))

    for song_id in list_ids:
        url = 'http://localhost:3000/simi/playlist?id=' + str(song_id)
        print('enter:',url)
        get_simi_music(url,user_id)
    
    df1 = pd.read_csv(filename1)
    list_ids = df1['list_id']
    counts = list_ids.value_counts()
    top_8 = counts.head(10).index.tolist()
    filtered_rows = df1[df1['list_id'].isin(top_8)]
    deduplicated = filtered_rows.drop_duplicates(subset='list_id')
    deduplicated.to_csv(f'Plate_1/data/recommend_list/output_{user_id}.csv', index=False)
