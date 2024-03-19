import mysql.connector as connection
from sqlalchemy import VARCHAR
mydb=connection.connect(host="localhost",user="root",passwd="11223344")
print(mydb)
cursor=mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())
