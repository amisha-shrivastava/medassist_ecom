import pymysql as MySql
try:
 CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123',database="studentmanagement")
 #CN is an object which contains address of Database Engine
 CMD=CN.cursor()
 #CMD is an Object use to supply query to Database Engine

 Q="select * from student"
 CMD.execute(Q)
 records=CMD.fetchall()
 #print(records)
 for row in records:
     print(row)
 CN.close()
except Exception as e:
    print(e)
