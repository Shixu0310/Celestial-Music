'''
author:Chenxu Zhang
date:2023.06.19
description:获取作者的热门歌曲的热门评论，直接整理成txt再做后续处理
'''
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# 获得热门评论的信息，并储存至txt
def get_top100(url,artist_id):
    r = requests.get(url)
    soup = r.json()
    filecomments = f'Plate_2/data/comments/top100_comments_{artist_id}.txt'
    for comments in soup['hotComments']:
        comment = comments['content'].replace('\n', '')
        with open(filecomments, 'a', encoding='utf-8-sig', newline='') as f:
            try:
                f.write(comment+" ")
            except Exception as msg:
                print(msg)

#获得前五首歌的热门评论以及评论者的相关信息
def get_5_comments(url,artist_id):
    r = requests.get(url)
    soup = r.json()
    try:
        comment = soup['hotComments'][0]['content'].replace('\n', '')
        name = soup['hotComments'][0]['user']['nickname']
        user_url = soup['hotComments'][0]['user']['avatarUrl']
    except:
        comment = 'This comment has been invaded by me'
        name = 'Silver Wolf'
        user_url = 'static/picture/hanser.png'
    #储存至csv文件中
    filecomments = f'Plate_2/data/comments_inf/top5_comments_{artist_id}.csv'
    with open(filecomments, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((name,user_url,comment))    

#还是一个小小的csv读入工具
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
    limit = 20
    offsets = [0]
    filename = f'Plate_2/data/artist_music/artist_{artist_id}.csv'
    song_ids = read_csv_column(filename, 'song_id')
    
    #获取作者的热门歌曲热评（全部）
    filecomments = f'Plate_2/data/comments/top100_comments_{artist_id}.txt'
    with open(filecomments, 'w', encoding='utf-8-sig', newline='') as f:
        pass
    for song_id in song_ids:
        for offset in offsets:
            url = 'http://localhost:3000/comment/music?id=' + str(song_id) + '&limit=' + str(limit) + '&offset=' + str(offset)
            print('enter:',url)
            get_top100(url,artist_id)

    #获取前5首歌top1热评信息
    filecomments5 = f'Plate_2/data/comments_inf/top5_comments_{artist_id}.csv'
    with open(filecomments5, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('user_name','user_url','comment'))

    for song_id in song_ids:
        url = 'http://localhost:3000/comment/music?id=' + str(song_id) + '&limit=' + str(limit) + '&offset=0'
        print('enter:',url)
        get_5_comments(url,artist_id)
    
    


