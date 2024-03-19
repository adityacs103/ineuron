from flask import Flask, request,jsonify
import mysql.connector as conn


app=Flask(__name__)

mydb=conn.connect(host="localhost",user='root',passwd="11223344")
cursor=mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.taktable (name varchar(30), number int)")

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=='POST':
      name=request.json['name']
      number=request.json['number']
      cursor.execute("insert into taskdb.taktable values(%s, %s)",(name,number))
      mydb.commit()
      return jsonify(str('succefullly inserted'))

@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        get_neme=request.json['get_name']
        cursor.execute("update taskdb.taktable set number = number + 50 where name =%s ",(get_neme,))
        mydb.commit()
        return jsonify(str("update successfully"))

@app.route("/delete",methods=['POST'])
def delete():
    if request.method=='POST':
        name_del=request.json['name_del']
        cursor.execute("delete from taskdb.taktable where name = %s",(name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))

@app.route('/fetch_data',methods=['POST'])
def fetch_data():
    l=[]
    cursor.execute("select * from taskdb.taktable")
    for i in cursor.fetchall():
        l.append(i)
        return jsonify(str(l))


if __name__=='__main__':
    app.run()  

