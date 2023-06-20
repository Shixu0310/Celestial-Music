'''
author:Chenxu Zhang
date:2023.06.19
description:此处获取音乐的tag
'''
import requests
from bs4 import BeautifulSoup
import csv

# 构造函数获取用户听歌的tag信息
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

#小工具读取csv文件
def read_csv_column(csv_file, column_name):
    data = []
    with open(csv_file, 'r',encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                data.append(row[column_name])
    return data

#主函数
def main(user_id):
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    song_ids = read_csv_column(filename, 'song_id')
    tag_all = []
    #遍历所有用户喜爱的歌曲
    for song_id in song_ids:
        url = 'http://localhost:3000/song/wiki/summary?id=' + str(song_id)
        print('enter:',url)
        tag_ls = get_tag(url)
        tag_all.extend(tag_ls)
    #统计tag个数
    label_counts = {}
    for label in tag_all:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    #写入csv文件
    with open(f'Plate_3/data/tag_count/tag_counts_{user_id}.csv', 'w', newline='',encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['tag', 'Count'])  # 写入标题行
        for label, count in label_counts.items():
            writer.writerow([label, count])
