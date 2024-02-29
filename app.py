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
@app.route("/vgh1", methods=['GET', 'POST'])
def vgh1():
    return render_template("/vugiahung/vgh1.html")
@app.route("/vgh2/", methods=['GET'])
def vgh2():
    return render_template("/vugiahung/vgh2.html")

if __name__ == '__main__':
   app.run()
