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
@app.route("/draft2/", methods=['GET'])
def ny2():
    return render_template("ny2.html")
@app.route("/ny3/", methods=['GET'])
def ny3():
    return render_template("ny3.html")
@app.route("/ny4/", methods=['GET'])
def ny4():
    return render_template("ny4.html")
@app.route("/ny5/", methods=['GET'])
def ny5():
    return render_template("ny5.html")
@app.route("/ny6/", methods=['GET'])
def ny6():
    return render_template("ny6.html")

#-----------------(thaophuongne1)
@app.route("/dGhhb3BodW9uZ25lMTM=/", methods=['GET'])
def thaophuongne1():
    return render_template("thaophuongne1.html")
@app.route("/dGhhb3BodW9uZ25lMTM=1/", methods=['GET'])
def thaophuongne2():
    return render_template("thaophuongne2.html")

if __name__ == '__main__':
   app.run()