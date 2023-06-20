'''
author:Chenxu Zhang
date:2023.06.19
description:这里是3区的主控代码,完成送入app.py前的数据处理
'''
import Plate_3.get_artistimg_top10 as get_artist
import Plate_3.get_music_tag as get_tag
import Plate_3.get_top100_comments as get_comment
import Plate_3.get_user_inf as get_inf
import Plate_3.get_user_music_top100 as get_music
import Plate_3.make_worldcloud as wordcloud
import pandas as pd

#获取用户的基本信息
def user_inf(user_id):
    return get_inf.main(user_id)

#三区爬虫
def user_spider(user_id):
    print("尝试获取top100歌曲")
    get_music.main(user_id)
    print("获取成功")
    print("===================================")
    print("尝试获取歌曲热评")
    get_comment.main(user_id)
    print("获取热评成功")
    print("===================================")
    print("尝试获取歌曲tag")
    get_tag.main(user_id)
    print("获取tag成功")
    print("===================================")
    print("尝试获取歌手top10")
    get_artist.main(user_id)
    print("获取歌手top10成功")

#获取所有歌曲的tag的前十，用于网页展示
def make_tag_list10(user_id):
    filename = f'Plate_3/data/tag_count/tag_counts_{user_id}.csv'
    data = pd.read_csv(filename)
    sorted_data = data.sort_values(by='Count', ascending=False)
    top_10 = sorted_data.head(10)
    result = []
    for _, row in top_10.iterrows():
        result.append({'value': row['Count'], 'name': row['tag']})
    return result

#获取所有用户常听的歌曲，这里是网页格式使用板块
def make_music_list100(user_id):
    filename = f'Plate_3/data/music_top100/user_{user_id}_top100.csv'
    data = []
    value = []
    name = []
    df = pd.read_csv(filename)
    selected_rows = df[['song_name', 'play_count']]
    for _, row in selected_rows.iterrows():
        data.append({'value': int(row['play_count']), 'name': row['song_name']})
        value.append(int(row['play_count']))
        name.append(row['song_name'])
    reslut = {"name":name,"value":value}
    return data,reslut

#制作一下词云图（作者的）
def make_word_cloud(user_id):
    wordcloud.main(user_id)

#获取用户喜爱歌曲评论的信息
def get_comment_inf(user_id):
    filename = f'Plate_3/data/comments_inf/top5_comments_{user_id}.csv'
    data = []
    df = pd.read_csv(filename)
    for _, row in df.iterrows():
        data.append({'user_url': row['user_url'], 'name': row['user_name'], 'comment': row['comment']})
    return data

#获取用户最喜爱的10个作者
def get_artist_top10(user_id):
    filename = f'Plate_3/data/artist/top10_img_{user_id}.csv'
    data = []
    df = pd.read_csv(filename)
    selected_rows = df[['artist_name', 'img_url','artist_id']]   
    for index, row in selected_rows[:4].iterrows():
        data.append({'name1': row['artist_name'], 'url1': row['img_url'], 'artist_id1': row['artist_id']})
    for index, row in selected_rows[5:9].iterrows():
        data[index-5]['name2'] = row['artist_name']
        data[index-5]['url2'] = row['img_url']
        data[index-5]['artist_id2'] = row['artist_id']
    return data

