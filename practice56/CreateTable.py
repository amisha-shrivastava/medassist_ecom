import pymysql as MySql
try:
 CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123',database="studentmanagement")
 #CN is an object which contains address of Database Engine
 CMD=CN.cursor()
 #CMD is an Object use to supply query to Database Engine
 Q="Create table student (rollno varchar(10) primary key,studentname varchar(40),dob date,gender varchar(10))"
 CMD.execute(Q)
 CN.commit()
 print("Table Created")
 CN.close()
except Exception as e:
    print(e)
