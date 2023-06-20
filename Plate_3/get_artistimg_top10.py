'''
author:Chenxu Zhang
date:2023.06.19
description:此处获得用户喜爱的作者top10
'''
import requests
from bs4 import BeautifulSoup
import csv

# 构造函数获取用户前100听歌记录
def get_top10_img(url,user_id,artist_id):
    r = requests.get(url)
    soup = r.json()
    filecomments = f'Plate_3/data/artist/top10_img_{user_id}.csv'
    imgs = soup['artist']
    img = imgs['picUrl']
    name = imgs['name']
    with open(filecomments, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        try:
            writer.writerow((artist_id,name,img))
        except Exception as msg:
            print(msg)

#小工具，用来读取csv
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
    #确定文件位置
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    artist_ids = read_csv_column(filename, 'artist_id')[:10]
    # 文件存储的位置
    filecomments = f'Plate_3/data/artist/top10_img_{user_id}.csv'
    with open(filecomments, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('artist_id','artist_name','img_url'))
    #开始获取数据
    for artist_id in artist_ids:
        url = 'http://localhost:3000/artists?id=' + str(artist_id)
        print('enter:',url)
        get_top10_img(url,user_id,artist_id)

