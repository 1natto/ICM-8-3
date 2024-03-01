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

#1
@app.route("/dG5uaDE=/", methods=['GET'])
def tnnh1():
    return render_template("tnnh1.html")
@app.route("/dG5uaDE=2/", methods=['GET'])
def tnnh2():
    return render_template("tnnh2.html")

#2
@app.route("/dG5uaDE=3/", methods=['GET'])
def tnnh3():
    return render_template("tnnh3.html")
@app.route("/dG5uaDE=4/", methods=['GET'])
def tnnh4():
    return render_template("tnnh4.html")

#3
@app.route("/dG5uaDE=5/", methods=['GET'])
def tnnh5():
    return render_template("tnnh5.html")
@app.route("/dG5uaDE=6/", methods=['GET'])
def tnnh6():
    return render_template("tnnh6.html")

#4
@app.route("/dG5uaDE=7/", methods=['GET'])
def tnnh7():
    return render_template("tnnh7.html")
@app.route("/dG5uaDE=8/", methods=['GET'])
def tnnh8():
    return render_template("tnnh8.html")

#5
@app.route("/dG5uaDE=9/", methods=['GET'])
def tnnh9():
    return render_template("tnnh9.html")
@app.route("/dG5uaDE=10/", methods=['GET'])
def tnnh10():
    return render_template("tnnh10.html")

#6
@app.route("/dG5uaDE=11/", methods=['GET'])
def tnnh11():
    return render_template("tnnh11.html")
@app.route("/dG5uaDE=12/", methods=['GET'])
def tnnh12():
    return render_template("tnnh12.html")


#7
@app.route("/dG5uaDE=13/", methods=['GET'])
def tnnh13():
    return render_template("tnnh13.html")
@app.route("/dG5uaDE=14/", methods=['GET'])
def tnnh14():
    return render_template("tnnh14.html")

#8

@app.route("/dG5uaDE=15/", methods=['GET'])
def tnnh15():
    return render_template("tnnh15.html")
@app.route("/dG5uaDE=16/", methods=['GET'])
def tnnh16():
    return render_template("tnnh16.html")


#----------tamanhpham

@app.route("/dGFwMQ==/", methods=['GET'])
def tap1():
    return render_template("tap1.html")
@app.route("/dGFwMQ==2/", methods=['GET'])
def tap2():
    return render_template("tap2.html")


#--------anchi

@app.route("/YW5jaGkx/", methods=['GET'])
def anchi1():
    return render_template("anchi1.html")
@app.route("/YW5jaGkx2/", methods=['GET'])
def anchi2():
    return render_template("anchi2.html")


if __name__ == '__main__':
   app.run()
