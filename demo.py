import datetime
from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/')
def Nav1():
    return render_template("index1.html")

@app.route('/URL1')
def Nav2():
    return render_template("register.html")