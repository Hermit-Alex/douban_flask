# -*- coding = utf-8 -*-
# @Time : 2020/8/27 19:25
# @Author : Hermit 
# @Fill : SQLtest.py
# @software : PyCharm
import sqlite3


def 计算评分结果(path):
    score = []
    number = []
    conn = sqlite3.connect(path)  # 有则联结 没有则创建该数据库
    print('成功打开/建立数据库！')
    c = conn.cursor()  # 获取游标 游标是查询数据库后查询到的结果
    sql = '''
        select score ,count(score) 
        from movie250
        group by score
        order by score desc ;
    '''  # SQL语句
    cursor = c.execute(sql)  # 执行SQL语句
    for item in cursor:
        score.append(item[0])
        number.append(item[1])
    for i in range(len(score)):
        score[i] = ''+ str(score[i])+''
    print(score,number)
    conn.commit()#结束数据库事务
    conn.close()#关闭连接
    print('成功查询数据！')



if __name__ == '__main__':
    path = "movie.db"
    计算评分结果(path)
