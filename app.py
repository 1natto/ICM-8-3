from flask import Flask, render_template, request, redirect, url_for, Response
import os

app = Flask(__name__)

#-----------default ny
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
@app.route("/draft1/", methods=['GET'])
def submit():
    return render_template("submit.html")

#-----------------(vugiahung)
@app.route("/vgh1/", methods=['GET'])
def vgh1():
    return render_template("vgh1.html")
@app.route("/vgh2/", methods=['GET'])
def vgh2():
    return render_template("vgh2.html")

#--------------(vuanhminhkhoi)
@app.route("/namk1/", methods=['GET'])
def namk1():
    return render_template("namk1.html")
@app.route("/namk2/", methods=['GET'])
def namk2():
    return render_template("namk2.html")

if __name__ == '__main__':
   app.run()
