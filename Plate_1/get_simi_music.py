'''
author:Chenxu Zhang
date:2023.06.19
description:这里是一区用于获取相似歌曲的板块，在这里给用户推荐相似的歌曲
'''
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# 构造函数获取用户常听歌曲的所有相似歌曲
def get_simi_music(url,user_id):
    r = requests.get(url)
    soup = r.json()
    filename1 = f"Plate_1/data/simi_music/simi_music_{user_id}.csv"
    try:
        songs = soup['songs']
    except:
        return
    with open(filename1, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        for song in songs:
            try:
                song_id = song['id']
                song_name = song['name']
                song_url = song['album']['picUrl']
                score = song['score']
                artist_name = song['artists'][0]['name']
                artist_id = song['artists'][0]['id']
                writer.writerow((song_id,song_name,score,song_url,artist_name,artist_id))
            except:
                continue
            
#读入csv的构造函数
def read_csv_column(csv_file, column_name):
    data = []
    with open(csv_file, 'r',encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                data.append(row[column_name])
    return data

#主函数，完成主要内容
def main(user_id):
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    song_ids = read_csv_column(filename, 'song_id')
    filename1 = f"Plate_1/data/simi_music/simi_music_{user_id}.csv"
    with open(filename1, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('song_id','song_name','score','song_url','artist_name','artist_id'))

    for song_id in song_ids:
        url = 'http://localhost:3000/simi/song?id=' + str(song_id)
        print('enter:',url)
        get_simi_music(url,user_id)
    
    #这里是在对推荐列表做筛选，去掉重复以及用户本来就听的歌，取出最多推荐的top8
    filename1 = f"Plate_1/data/simi_music/simi_music_{user_id}.csv"
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename)
    df1 = df1[~df1['song_id'].isin(df2['song_id'])]
    song_ids = df1['song_id']
    counts = song_ids.value_counts()
    top_8 = counts.head(8).index.tolist()
    filtered_rows = df1[df1['song_id'].isin(top_8)]
    deduplicated = filtered_rows.drop_duplicates(subset='song_id')
    deduplicated.to_csv(f'Plate_1/data/recommend/output_{user_id}.csv', index=False)
