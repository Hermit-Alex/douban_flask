# -*- coding = utf-8 -*-
# @Time : 2020/8/27 22:24
# @Author : Hermit 
# @Fill : TestWordCloud.py
# @software : PyCharm

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

def conn_sql():
    text = ""
    conn = sqlite3.connect('movie.db')
    cursor = conn.cursor()
    sql = '''
    select intro 
    from movie250
    '''
    data = cursor.execute(sql)
    for item in data:
        text = text + item[0]
    cursor.close()
    conn.commit()
    conn.close()
    return text

if __name__ == '__main__':
    #准备好输入到词云的词
    text = conn_sql()
    #分词操作
    cut = jieba.cut(text)
    string = ' '.join(cut)#一共分出5642个词
    img = Image.open(r'./static/assets/img/pkq.jpg')
    img_array = np.array(img)#将图片转换为数组
    wc = WordCloud(
        background_color= 'white',
        mask = img_array,
        font_path= "STHUPO.TTF"#SHOWG.TTF
    )#设置好背景遮罩图片字体
    wc.generate_from_text(string)
    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()#显示生成的词云图
    plt.savefig(r'./static/assets/img/word.png')
    print("save successfully!")