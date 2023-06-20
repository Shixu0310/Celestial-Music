'''
author:Chenxu Zhang
date:2023.06.19
description:此处获得用户喜爱歌曲的热门评论
'''
import requests
from bs4 import BeautifulSoup
import csv

# 构造函数来获得怕所有歌曲的评论信息
def get_top100(url,user_id):
    r = requests.get(url)
    soup = r.json()
    filecomments = f'Plate_3/data/comments/top100_comments_{user_id}.txt'
    for comments in soup['hotComments']:
        comment = comments['content'].replace('\n', '')
        with open(filecomments, 'a', encoding='utf-8-sig', newline='') as f:
            try:
                f.write(comment+" ")
            except Exception as msg:
                print(msg)

#主要获得前五的评论内容，包括评论人的基本信息
def get_5_comments(url,user_id):
    r = requests.get(url)
    soup = r.json()
    comment = soup['hotComments'][0]['content'].replace('\n', '')
    name = soup['hotComments'][0]['user']['nickname']
    user_url = soup['hotComments'][0]['user']['avatarUrl']
    filecomments = f'Plate_3/data/comments_inf/top5_comments_{user_id}.csv'
    with open(filecomments, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((name,user_url,comment))    

#小工具用于读取csv文件
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
    limit = 20
    offsets = [0]
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    song_ids = read_csv_column(filename, 'song_id')
    #获取用户热评（全部）
    filecomments = f'Plate_3/data/comments/top100_comments_{user_id}.txt'
    with open(filecomments, 'w', encoding='utf-8-sig', newline='') as f:
        pass
    for song_id in song_ids:
        for offset in offsets:
            url = 'http://localhost:3000/comment/music?id=' + str(song_id) + '&limit=' + str(limit) + '&offset=' + str(offset)
            print('enter:',url)
            get_top100(url,user_id)

    #获取前5首歌top1热评信息
    filecomments5 = f'Plate_3/data/comments_inf/top5_comments_{user_id}.csv'
    with open(filecomments5, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('user_name','user_url','comment'))
        
    #筛选前五的信息存入csv
    for song_id in song_ids[:5]:
        url = 'http://localhost:3000/comment/music?id=' + str(song_id) + '&limit=' + str(limit) + '&offset=0'
        print('enter:',url)
        get_5_comments(url,user_id)
