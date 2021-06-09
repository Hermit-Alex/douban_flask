from flask import Flask,render_template,request
import sqlite3


app = Flask(__name__)
#上面的代码作用为引入flask框架

# /访问路径
@app.route('/temp')
def hello_world():
    return render_template("temp.html")

@app.route('/')
def first():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("movie.db")#连接 有数据库就连接 没有就创建
    cursor = conn.cursor()#获取游标
    sql = '''
    select * from movie250
    '''
    data = cursor.execute(sql)#执行SQL语句
    for item in data:
        datalist.append(item)
    conn.commit()#结束数据库事务
    conn.close()#关闭连接
    return render_template("movie.html",list = datalist)


@app.route('/score')

def score():
    score = []
    number = []
    conn = sqlite3.connect("movie.db")  # 有则联结 没有则创建该数据库
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
    conn.commit()#结束数据库事务
    conn.close()#关闭连接

    return render_template("score.html",score = score,number =number )

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/word')
def word():
    return render_template("word.html")








if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
