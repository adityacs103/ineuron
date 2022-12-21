#this is for insert data in mongodb
from flask import Flask, request,jsonify
import pymongo
app=Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://aditya_project:11223344@cluster0.ezqelc1.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client['taskdb']
collection=database['taskcollection']

@app.route("/insert",methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("succefully inserted"))

if __name__=='__main__':
    app.run(port=5001)
