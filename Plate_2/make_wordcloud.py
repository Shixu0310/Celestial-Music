'''
author:Chenxu Zhang
date:2023.06.19
description:此处制作作者评论区的热词词云图
'''
import jieba.posseg as pseg
import re
import pandas as pd
import matplotlib.pyplot as plt
from os import path
from imageio import imread
from wordcloud import WordCloud

#获得词云图
def extract_words(comment_subjects,artist_id):
    #加载stopword
    stop_words = set(line.strip() for line in open('Plate_2/data/stopwords.txt', encoding='utf-8-sig'))
    commentlist = []
    for subject in comment_subjects:
        if subject.isspace():continue
        # 读入stopwords
        word_list = pseg.cut(subject)#分词
        for word, flag in word_list:
            if not word in stop_words and flag == 'n':
                #添加有效词
                commentlist.append(word)
    
    mask_image = imread("Plate_2/data/test3.png")#加载模板图片
    content = ' '.join(commentlist)
    #绘制词云图
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="white",  mask=mask_image, max_words=200).generate(content)
    plt.imshow(wordcloud)
    plt.axis("off")
    #保存在合适的地址
    wordcloud.to_file(f'static/image/wordcloud_part2/wordcloud_part2_{artist_id}.jpg')

#主函数
def main(artist_id):
    with open(f'Plate_2/data/comments/top100_comments_{artist_id}.txt','r',encoding='utf-8') as f:
        comment_subjects = f.readlines()
    extract_words(comment_subjects,artist_id)
