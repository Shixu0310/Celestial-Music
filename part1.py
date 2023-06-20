'''
author:Chenxu Zhang
date:2023.06.19
description:这里是一区的主控代码,完成送入app.py前的数据处理
'''
import Plate_1.get_simi_music as get_simi_music
import Plate_1.get_simi_playlist as get_simi_playlist
import pandas as pd

#启动一区爬虫
def recommend_spider(user_id):
    print("尝试获取相似歌曲")
    get_simi_music.main(user_id)
    print("获取成功")
    print("===================================")
    print("尝试获取相似歌单")
    get_simi_playlist.main(user_id)
    print("获取成功")
    print("===================================")

#获取推荐的歌曲数据，并整理成html文件中需要的格式
def get_recommend_data(user_id):
    filename = f'Plate_1/data/recommend/output_{user_id}.csv'
    df = pd.read_csv(filename)
    data1 = []
    for index, row in df[:2].iterrows():
        data1.append({'song_name1': row['song_name'], 
                     'song_url1': row['song_url'],
                       'artist_id1': row['artist_id'],
                       'song_id1': row['song_id'],
                       'artist_name1': row['artist_name'],
                       'score1':row['score']})
        
    for index, row in df[2:4].iterrows():
        data1[index-2]['song_name2'] = row['song_name']
        data1[index-2]['song_url2'] = row['song_url']
        data1[index-2]['artist_id2'] = row['artist_id']
        data1[index-2]['artist_name2'] = row['artist_name']
        data1[index-2]['score2'] = row['score']
        data1[index-2]['song_id2'] = row['song_id']
    
    data2 = []
    for index, row in df[4:6].iterrows():
        data2.append({'song_name1': row['song_name'], 
                     'song_url1': row['song_url'],
                       'artist_id1': row['artist_id'],
                       'song_id1': row['song_id'],
                       'artist_name1': row['artist_name'],
                       'score1':row['score']})
        
    for index, row in df[6:8].iterrows():
        data2[index-6]['song_name2'] = row['song_name']
        data2[index-6]['song_url2'] = row['song_url']
        data2[index-6]['artist_id2'] = row['artist_id']
        data2[index-6]['artist_name2'] = row['artist_name']
        data2[index-6]['score2'] = row['score']
        data2[index-6]['song_id2'] = row['song_id']
    
    return data1,data2#两个list是因为网页上有两个板块

#获取推荐歌单列表,控制格式
def get_recommend_playlist(user_id):
    filename = f'Plate_1/data/recommend_list/output_{user_id}.csv'
    df = pd.read_csv(filename)
    data = []
    for _, row in df.iterrows():
        data.append({'list_url': row['list_url'],
                    'list_name': row['list_name'], 
                    'list_tag': row['list_tag'],
                    'list_des': row['list_des']
                    })
    return data
