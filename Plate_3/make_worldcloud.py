'''
author:Chenxu Zhang
date:2023.06.19
description:此处制作用户常听歌曲的评论的词云图
'''
import jieba.posseg as pseg
import re
import pandas as pd
import matplotlib.pyplot as plt
from os import path
from imageio import imread
from wordcloud import WordCloud

#制作词云图
def extract_words(comment_subjects,user_id):
    #加载stopword
    stop_words = set(line.strip() for line in open('Plate_3/data/stopwords.txt', encoding='utf-8-sig'))
    commentlist = []
    for subject in comment_subjects:
        if subject.isspace():continue
        word_list = pseg.cut(subject)#分词
        for word, flag in word_list:
            if not word in stop_words and flag == 'n':
                commentlist.append(word)
    
    mask_image = imread("Plate_3/data/test.png")
    content = ' '.join(commentlist)
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="white",  mask=mask_image, max_words=200).generate(content)
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file(f'static/image/wordcloud_part3/wordcloud_part3_{user_id}.jpg')

#主函数
def main(user_id):
    with open(f'Plate_3/data/comments/top100_comments_{user_id}.txt','r',encoding='utf-8') as f:
        comment_subjects = f.readlines()
    extract_words(comment_subjects,user_id)

