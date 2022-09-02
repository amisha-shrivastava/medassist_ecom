import pymysql as MySql
try:
 CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123',database="studentmanagement")
 #CN is an object which contains address of Database Engine
 CMD=CN.cursor()
 #CMD is an Object use to supply query to Database Engine
 rollno=input("Enter Roll Number:")
 Q="select * from student where rollno='{0}'".format(rollno)
 CMD.execute(Q)
 record=CMD.fetchone()
 if(record):
     print(record)
 else:
   print('Record Not Found')

 CN.close()
except Exception as e:
    print(e)
