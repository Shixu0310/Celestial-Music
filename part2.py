'''
author:Chenxu Zhang
date:2023.06.19
description:这里是2区的主控代码,完成送入app.py前的数据处理
'''
import Plate_2.get_artists_inf as get_artist_inf
import Plate_2.get_artist_music as get_artist_music1
import Plate_2.get_comment as get_comment
import Plate_2.get_music_tag as get_tag
import Plate_2.make_wordcloud as make_wordcloud
import Plate_2.get_xzqh_json as get_xzqh
import pandas as pd

#获取作者的基本信息用于网页展示，同时也可以用于查看输入是否合法
def artist_inf(artist_id):
    data_inf,data_list,all_value = get_artist_inf.main(artist_id)
    data_list.append({'value':all_value , 'itemStyle':{'color': 'none','decal': {'symbol': 'none'}},'label':{'show': 'false'}})
    return data_inf,data_list

#二区爬虫
def artist_spider(artist_id):
    print("开始爬取作者热门歌曲")
    get_artist_music1.main(artist_id)
    print("爬取完成")
    print("==================================")
    print("开始爬取热门歌曲评论")
    get_comment.main(artist_id)
    print("爬取完成")
    print("==================================")
    print("开始爬取歌曲tag")
    get_tag.main(artist_id)
    print("爬取完成")
    print("==================================")
    print("开始制作")
    make_wordcloud.main(artist_id)
    print("制作完成")
    print("==================================")

#获取评论信息，用于制作网页中的评论的list
def get_comment_inf(artist_id):
    filecomments5 = f'Plate_2/data/comments_inf/top5_comments_{artist_id}.csv'
    filename = f'Plate_2/data/artist_music/artist_{artist_id}.csv'
    df = pd.read_csv(filecomments5)
    data = []
    for _, row in df.iterrows():
        data.append({'user_url': row['user_url'], 'name': row['user_name'], 'comment': row['comment']})
    
    df1 = pd.read_csv(filename)
    for index, row in df1.iterrows():
        data[index]['song_name'] = row['song_name']
        data[index]['song_url'] = row['song_url']
    return data
    
#获取歌曲的tag用于补充数据库同时可以进行网页展示
def get_artist_music_tag(artist_id):
    filename = f'Plate_2/data/tag_count/tag_counts_{artist_id}.csv'
    value = []
    name = []
    df = pd.read_csv(filename)
    for _, row in df.iterrows():
        value.append(int(row['Count']))
        name.append(row['tag'])
    reslut = {"name":name,"value":value}
    return reslut   

#控制获取作者粉丝的坐标位置以及性别的数据，属于中转板块
def make_fan_inf(artist_id):
    new_loc,new_gender = get_xzqh.main(artist_id)
    new_dict = get_xzqh.generate_new_dictionary()
    return new_loc,new_gender,new_dict

