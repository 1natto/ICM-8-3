from flask import Flask, render_template, request, redirect, url_for, Response
import os

app = Flask(__name__)

#----------default ny
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("a1.html")
@app.route("/draft1/", methods=['GET'])
def submit():
    return render_template("a2.html")

#1
@app.route("/dmdoMQ==/", methods=['GET'])
def vgh1():
    return render_template("vgh1.html")
@app.route("/dmdoMQ==2/", methods=['GET'])
def vgh2():
    return render_template("vgh2.html")

#2
@app.route("/bmFtazE=/", methods=['GET'])
def namk1():
    return render_template("namk1.html")
@app.route("/bmFtazE=2/", methods=['GET'])
def namk2():
    return render_template("namk2.html")

#3
@app.route("/dG5uaDE=/", methods=['GET'])
def tnnh1():
    return render_template("tnnh1.html")
@app.route("/dG5uaDE=2/", methods=['GET'])
def tnnh2():
    return render_template("tnnh2.html")

#4
@app.route("/dG5uaDE=3/", methods=['GET'])
def tnnh3():
    return render_template("tnnh3.html")
@app.route("/dG5uaDE=4/", methods=['GET'])
def tnnh4():
    return render_template("tnnh4.html")

#5
@app.route("/dG5uaDE=5/", methods=['GET'])
def tnnh5():
    return render_template("tnnh5.html")
@app.route("/dG5uaDE=6/", methods=['GET'])
def tnnh6():
    return render_template("tnnh6.html")

#6
@app.route("/dG5uaDE=7/", methods=['GET'])
def tnnh7():
    return render_template("tnnh7.html")
@app.route("/dG5uaDE=8/", methods=['GET'])
def tnnh8():
    return render_template("tnnh8.html")

#7
@app.route("/dG5uaDE=9/", methods=['GET'])
def tnnh9():
    return render_template("tnnh9.html")
@app.route("/dG5uaDE=10/", methods=['GET'])
def tnnh10():
    return render_template("tnnh10.html")

#8
@app.route("/dG5uaDE=11/", methods=['GET'])
def tnnh11():
    return render_template("tnnh11.html")
@app.route("/dG5uaDE=12/", methods=['GET'])
def tnnh12():
    return render_template("tnnh12.html")


#9
@app.route("/dG5uaDE=13/", methods=['GET'])
def tnnh13():
    return render_template("tnnh13.html")
@app.route("/dG5uaDE=14/", methods=['GET'])
def tnnh14():
    return render_template("tnnh14.html")

#10

@app.route("/dG5uaDE=15/", methods=['GET'])
def tnnh15():
    return render_template("tnnh15.html")
@app.route("/dG5uaDE=16/", methods=['GET'])
def tnnh16():
    return render_template("tnnh16.html")

#11
@app.route("/aHRxYTE=/", methods=['GET'])
def htqa1():
    return render_template("htqa1.html")
@app.route("/aHRxYTE=2/", methods=['GET'])
def htqa2():
    return render_template("htqa2.html")

#12
@app.route("/dGJtMQo=/", methods=['GET'])
def tbm1():
    return render_template("tbm1.html")
@app.route("/dGJtMQo=2/", methods=['GET'])
def tbm2():
    return render_template("tbm2.html")

#13
@app.route("/bnTEkQ/", methods=['GET'])
def ntd1():
    return render_template("ntd1.html")
@app.route("/bnTEkQ==/", methods=['GET'])
def ntd2():
    return render_template("ntd2.html")

#14
@app.route("/bnBsQMo=/", methods=['GET'])
def npl1():
    return render_template("npl1.html")
@app.route("/bnBsQMo=2/", methods=['GET'])
def npl2():
    return render_template("npl2.html")

#15
@app.route("/cGts/", methods=['GET'])
def pkl1():
    return render_template("pkl1.html")
@app.route("/cGts2/", methods=['GET'])
def pkl2():
    return render_template("pkl2.html")

#16
@app.route("/bmwx/", methods=['GET'])
def nl1():
    return render_template("nl1.html")
@app.route("/bmwyCg==/", methods=['GET'])
def nl2():
    return render_template("nl2.html")

#17
@app.route("/dHJhbWE=/", methods=['GET'])
def ta1():
    return render_template("ta1.html")
@app.route("/dHJhbWE=2/", methods=['GET'])
def ta2():
    return render_template("ta2.html")

#18
@app.route("/a3QxCg==/", methods=['GET'])
def kt1():
    return render_template("kt1.html")
@app.route("/a3QyCg==/", methods=['GET'])
def kt2():
    return render_template("kt2.html")

#19
@app.route("/bnRobQo=/", methods=['GET'])
def nthm1():
    return render_template("nthm1.html")
@app.route("/bnRobQo=2/", methods=['GET'])
def nthm2():
    return render_template("nthm2.html")

#20
@app.route("/ZHBnbDEK/", methods=['GET'])
def dpgl1():
    return render_template("dpgl1.html")
@app.route("/ZHBnbDIK/", methods=['GET'])
def dpgl2():
    return render_template("dpgl2.html")

#21
@app.route("/dGhhdDE=/", methods=['GET'])
def that1():
    return render_template("that1.html")
@app.route("/dGhhdDE=2/", methods=['GET'])
def that2():
    return render_template("that2.html")

#22
@app.route("/Y2toMQo=/", methods=['GET'])
def ckh1():
    return render_template("ckh1.html")
@app.route("/Y2toMgo=/", methods=['GET'])
def ckh2():
    return render_template("ckh2.html")

#23
@app.route("/YW5jaGkx/", methods=['GET'])
def anchi1():
    return render_template("anchi1.html")
@app.route("/YW5jaGkx2/", methods=['GET'])
def anchi2():
    return render_template("anchi2.html")

#24
@app.route("/cHFoMQ==/", methods=['GET'])
def pqh1():
    return render_template("pqh1.html")
@app.route("/cHFoMg==/", methods=['GET'])
def pqh2():
    return render_template("pqh2.html")

#25
@app.route("/dHRsMjU=/", methods=['GET'])
def ttl25():
    return render_template("ttl25.html")
@app.route("/dHRsMjU=2/", methods=['GET'])
def ttl252():
    return render_template("ttl252.html")

#26
@app.route("/dG50bDI2Cg==/", methods=['GET'])
def tntl26():
    return render_template("tntl26.html")
@app.route("/dG50bDI2Mg==/", methods=['GET'])
def tntl262():
    return render_template("tntl262.html")

#27
@app.route("/cHFoMw==/", methods=['GET'])
def pqh3():
    return render_template("pqh3.html")
@app.route("/cHFoMw==2/", methods=['GET'])
def pqh4():
    return render_template("pqh4.html")

#28
@app.route("/bm10Mjg=/", methods=['GET'])
def nmt28():
    return render_template("nmt28.html")
@app.route("/bm10MjgyCg==/", methods=['GET'])
def nmt282():
    return render_template("nmt282.html")

#29
@app.route("/dGFwMQ==/", methods=['GET'])
def tap1():
    return render_template("tap1.html")
@app.route("/dGFwMQ==2/", methods=['GET'])
def tap2():
    return render_template("tap2.html")

#30
@app.route("/bG52MzA=/", methods=['GET'])
def lnv30():
    return render_template("lnv30.html")
@app.route("/bG52MzAyCg==/", methods=['GET'])
def lnv302():
    return render_template("lnv302.html")

#31

#32
@app.route("/bG5tYzMy/", methods=['GET'])
def lnmc32():
    return render_template("lnmc32.html")
@app.route("/bG5tYzMyMg==/", methods=['GET'])
def lnmc322():
    return render_template("lnmc322.html")

#33
@app.route("/bG1uCg==/", methods=['GET'])
def lmn1():
    return render_template("lmn1.html")
@app.route("/bG1uCg==2/", methods=['GET'])
def lmn2():
    return render_template("lmn2.html")

#34
@app.route("/Y2hiaDM0/", methods=['GET'])
def chbh34():
    return render_template("chbh34.html")
@app.route("/Y2hiaDI0Mg==/", methods=['GET'])
def chbh342():
    return render_template("chbh342.html")

#35
@app.route("/bnRoIA==/", methods=['GET'])
def nth1():
    return render_template("nth1.html")
@app.route("/bnRoIA==2/", methods=['GET'])
def nth2():
    return render_template("nth2.html")

#36
@app.route("/dG5wbDM2/", methods=['GET'])
def tnpl36():
    return render_template("tnpl36.html")
@app.route("/dG5wbDM2Mg==/", methods=['GET'])
def tnpl362():
    return render_template("tnpl362.html")

#37

#38
@app.route("/dmJoMzg=/", methods=['GET'])
def vbh38():
    return render_template("vbh38.html")
@app.route("/dmJoMzg===/", methods=['GET'])
def vbh382():
    return render_template("vbh382.html")

#39
@app.route("/Ym1wIA==/", methods=['GET'])
def bmp1():
    return render_template("bmp1.html")
@app.route("/Ym1wIA==2/", methods=['GET'])
def bmp2():
    return render_template("bmp2.html")

#40
@app.route("/cG5oYjQw/", methods=['GET'])
def pnhb40():
    return render_template("pnhb40.html")
@app.route("/cG5oYjQw==/", methods=['GET'])
def pnhb402():
    return render_template("pnhb402.html")

#41

#42
@app.route("/dHR0bDQy/", methods=['GET'])
def tttl42():
    return render_template("tttl42.html")
@app.route("/dHR0bDQy==/", methods=['GET'])
def tttl422():
    return render_template("tttl422.html")


#43

#44
@app.route("/YnQ0NA/", methods=['GET'])
def bt44():
    return render_template("bt44.html")
@app.route("/YnQ0NA==/", methods=['GET'])
def bt442():
    return render_template("bt442.html")

#45

#46
@app.route("/dnRrYzQ2/", methods=['GET'])
def vtkc46():
    return render_template("vtkc46.html")
@app.route("/dnRrYzQ2==/", methods=['GET'])
def vtkc462():
    return render_template("vtkc462.html")

#47

#48
@app.route("/bHR0NDg/", methods=['GET'])
def ltt48():
    return render_template("ltt48.html")
@app.route("/bHR0NDg==/", methods=['GET'])
def ltt482():
    return render_template("ltt482.html")

#49
@app.route("/Ym7EkQ==/", methods=['GET'])
def bnd1():
    return render_template("bnd1.html")
@app.route("/Ym7EkQ==2/", methods=['GET'])
def bnd2():
    return render_template("bnd2.html")

#50
@app.route("/aGRkdjUw/", methods=['GET'])
def hddv50():
    return render_template("hddv50.html")
@app.route("/aGRkdjUw==/", methods=['GET'])
def hddv502():
    return render_template("hddv502.html")

if __name__ == '__main__':
   app.run()

