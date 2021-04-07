import datetime
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    now=datetime.datetime.now()
    new_year=now.month == 1 and now.day == 1
    return render_template("index.html",new_year=new_year)


@app.route('/index')
def first():
    name="Sam"
    return render_template("index.html",headline=name)


@app.route('/first')
def first1():
    return "Goodbye"

@app.route('/second')
def second1():
    d=['Sam','Vishal','Mohan','Sai Kiran']
    return render_template("second1.html",name=d)
