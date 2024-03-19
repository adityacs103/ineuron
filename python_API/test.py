from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/add',methods=['GET','POST'])

def add():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify(str(result))


@app.route("/sub",methods=['GET','POST'])
def sub():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a-b
        return jsonify((str(result)))


@app.route("/multiply",methods=['GET','POST'])
def multiply():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a*b
        return jsonify((str(result)))


@app.route("/devide",methods=['GET','POST'])
def devide():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a/b
        return jsonify(result)


if __name__=='__main__':
    app.run()


