# -*- coding: utf-8-sig -*-
'''
author:Chenxu Zhang
date:2023.06.19
description:启动flask,网页跳转板块
'''
from flask import Flask,render_template,request
import part3
import part2
import part1
import os
import json
import subprocess
app = Flask(__name__)

#开始界面
@app.route("/")
def hello():
    return render_template("login.html")

#获取index页面的data，打开index页面
def index(user_id):
    user_inf = part3.user_inf(user_id)
    user_tag_top10 = part3.make_tag_list10(user_id)
    json_user_tag10 = json.dumps(user_tag_top10)
    music_top100,b = part3.make_music_list100(user_id)
    json_music_top100 = json.dumps(b)
    comment_inf = part3.get_comment_inf(user_id)
    wordcould_url_part3 = f"static/image/wordcloud_part3/wordcloud_part3_{user_id}.jpg"
    artist_list = part3.get_artist_top10(user_id) 
    return render_template("index.html",
                           user_name = user_inf[0],
                           user_signature = user_inf[1],
                           user_img = user_inf[2],
                           gender = user_inf[3],
                           viptype = user_inf[4],
                           hot1_music = user_inf[5],
                           user_id = user_id,
                           user_tag_10 = json_user_tag10,
                           user_tag_10_list = user_tag_top10,
                           user_music_top100 = music_top100,
                           json_user_music_top100 = json_music_top100,
                           comment_inf = comment_inf,
                           wordcould_url_part3 = wordcould_url_part3,
                           artist_top8 = artist_list
                           )

#获取artist页面的data，打开artist页面
def artist(user_id,artist_id):
    user_inf = part3.user_inf(user_id)
    new_loc,new_gender,new_dict = part2.make_fan_inf(artist_id)
    print(list(new_gender.keys()),list(new_gender.values()))
    b = part2.get_artist_music_tag(artist_id)
    json_music_top100 = json.dumps(b)
    wordcloud_part2 = f"static/image/wordcloud_part2/wordcloud_part2_{artist_id}.jpg"
    data_inf,data_list = part2.artist_inf(artist_id)
    json_artist_list = json.dumps(data_list)
    music_comment = part2.get_comment_inf(artist_id)
    return render_template("artist.html",
                           user_name = user_inf[0],
                           user_signature = user_inf[1],
                           user_img = user_inf[2],
                           gender = user_inf[3],
                           viptype = user_inf[4],
                           hot1_music = user_inf[5],
                           user_id = user_id,
                           json_user_music_top100 = json_music_top100,
                           back_url = data_inf[3],
                           artist_name = data_inf[1],
                           briefdesc = data_inf[2],
                           artist_img = data_inf[0],
                           wordcloud_part2 = wordcloud_part2,
                           artist_list_json = json_artist_list,
                           artist_list_abi = data_list,
                           music_comment = music_comment,
                           gender_name = list(new_gender.keys()),
                           gender_data = list(new_gender.values()),
                           new_loc = new_loc,
                           new_dict = new_dict
                           )

#检查输入的userid是否合法，合法则启动爬虫。非法id：404；爬取失败：500
@app.route("/index",methods = ['POST'])
def check_user():
    user_id = request.form.get('userId')
    try:
        part3.user_inf(user_id)
    except:
        return render_template("error-404.html")

    if os.path.exists(f"Plate_3/data/artist/top10_img_{user_id}.csv"):
        pass
    else:
        try:
            part3.user_spider(user_id)
        except:
            return render_template("error-500.html")
    if os.path.exists(f"static/image/wordcloud_part3/wordcloud_part3_{user_id}.jpg"):
        pass
    else:
        try:
            part3.make_word_cloud(user_id)
        except:
            return render_template("error-500.html")
    if os.path.exists(f'Plate_1/data/recommend_list/output_{user_id}.csv'):
        pass
    else:
        try:
            part1.recommend_spider(user_id)
        except:
            return render_template("error-500.html")
    return index(user_id)

#打开登录界面（同时也算是登出）
@app.route("/login")
def login():
    return render_template("login.html")

#打开help界面
@app.route("/help")
def help():
    return render_template("help.html")

#启动recommend界面
@app.route("/recommend",methods = ['POST'])
def recommend():
    user_id = request.form.get('userId')
    user_inf = part3.user_inf(user_id)
    artist_list = part3.get_artist_top10(user_id)
    recommend_list1,recommend_list2 = part1.get_recommend_data(user_id)
    playlist_data = part1.get_recommend_playlist(user_id)
    return render_template("recommend.html",
                            user_name = user_inf[0],
                            user_signature = user_inf[1],
                            user_id = user_id,
                            artist_top8 = artist_list,
                            recommend_list1 = recommend_list1,
                            recommend_list2 = recommend_list2,
                            playlist_data = playlist_data
                           )

#检查作者id是否合法
@app.route("/artist",methods = ['POST'])
def artist_check():
    user_id = request.form.get('userId')
    artist_id = request.form.get('artistId')
    try:
        part2.artist_inf(artist_id)
    except:
        return render_template('error-404.html')
    if os.path.exists(f'static/image/wordcloud_part2/wordcloud_part2_{artist_id}.jpg'):
        pass
    else:
        try:
            part2.artist_spider(artist_id)
        except:
            return render_template("error-500.html")
    return artist(user_id,artist_id)

#打开search界面
@app.route("/search",methods = ['POST'])
def search():
    user_id = request.form.get('userId')
    user_inf = part3.user_inf(user_id)
    artist_list = part3.get_artist_top10(user_id) 
    return render_template("search.html",
                            user_name = user_inf[0],
                            user_signature = user_inf[1],
                            user_id = user_id,
                            artist_top8 = artist_list
                           )


#主程序，启动原神（bushi），启动html
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)