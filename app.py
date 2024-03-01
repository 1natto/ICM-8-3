from flask import Flask, render_template, request, redirect, url_for, Response
import os

app = Flask(__name__)

#-----------default ny
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("a1.html")
@app.route("/draft1/", methods=['GET'])
def submit():
    return render_template("a2.html")

#-----------------(vugiahung)
@app.route("/dmdoMQ==/", methods=['GET'])
def vgh1():
    return render_template("vgh1.html")
@app.route("/dmdoMQ==2/", methods=['GET'])
def vgh2():
    return render_template("vgh2.html")

#--------------(vuanhminhkhoi)
@app.route("/bmFtazE=/", methods=['GET'])
def namk1():
    return render_template("namk1.html")
@app.route("/bmFtazE=2/", methods=['GET'])
def namk2():
    return render_template("namk2.html")

#---------Trần Nhân Nhật Minh








if __name__ == '__main__':
   app.run()
