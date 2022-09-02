import pymysql as MySql
try:
 CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123',database="studentmanagement")
 #CN is an object which contains address of Database Engine
 CMD=CN.cursor()
 #CMD is an Object use to supply query to Database Engine
 pat=input("Enter Pattern:")
 Q="select * from student where studentname like '%{0}%'".format(pat)
 CMD.execute(Q)
 records=CMD.fetchall()
 if(records):
     print(records)
 else:
   print('Record Not Found')

 CN.close()
except Exception as e:
    print(e)
