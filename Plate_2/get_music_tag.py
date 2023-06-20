'''
author:Chenxu Zhang
date:2023.06.19
description:分析作者的热门歌曲，并提取其中的所有tag，用来分析作者作曲的偏好
'''
import requests
from bs4 import BeautifulSoup
import csv

# 获得所有作者热门歌曲的tag
def get_tag(url):
    r = requests.get(url)
    soup = r.json()
    tag_ls = []
    try:
        tags = soup['data']['blocks'][1]['creatives'][1]['resources']
        for tag in tags:
            tag_true = tag['uiElement']['mainTitle']['title']
            tag_ls.append(tag_true)
        return tag_ls   
    except:
        return tag_ls

#读取csv文件的小工具
def read_csv_column(csv_file, column_name):
    data = []
    with open(csv_file, 'r',encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                data.append(row[column_name])
    return data

#主控函数
def main(artist_id):
    #打开csv文件，获取作者的热门歌曲列表
    filename = f'Plate_2/data/artist_music/artist_{artist_id}.csv'
    song_ids = read_csv_column(filename, 'song_id')
    tag_all = []
    for song_id in song_ids:
        url = 'http://localhost:3000/song/wiki/summary?id=' + str(song_id)
        print('enter:',url)
        tag_ls = get_tag(url)
        tag_all.extend(tag_ls)
    label_counts = {}
    #统计tag的个数
    for label in tag_all:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    #循环写入csv
    with open(f'Plate_2/data/tag_count/tag_counts_{artist_id}.csv', 'w', newline='',encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['tag', 'Count'])  # 写入标题行
        for label, count in label_counts.items():
            writer.writerow([label, count])

