from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

'''
将豆瓣数据可视化 找到index模板
'''


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return index()


@app.route('/movie')
def movie():  # 将数据库中数据取出即可
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=datalist)
    # return render_template("movie.html")

# 学习使用echarts请访问 https://echarts.apache.org/examples/zh/editor.html?c=bar-background


@app.route('/score')
def score():
    score2 = []
    num = []  # 每个评分统计出的电影数量
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    # 先手动查询执行下sql语句确保没问题
    sql = "select score ,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score2.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", score=score2, num=num)


@app.route('/team')
def team():
    return render_template("team.html")


#  词云 http://amueller.github.io/word_cloud/auto_examples/wordcloud_cn.html
@app.route('/word')
def word():
    return render_template("word.html")


if __name__ == '__main__':
    app.run()
