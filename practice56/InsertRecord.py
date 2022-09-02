import pymysql as MySql
try:
 CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123',database="studentmanagement")
 #CN is an object which contains address of Database Engine
 CMD=CN.cursor()
 #CMD is an Object use to supply query to Database Engine
 rollno=input("Enter Rollno:")
 name = input("Enter Name:")
 dob = input("Enter Birth Date:")
 gender = input("Enter Gender:")

 Q="insert into student values('{0}','{1}','{2}','{3}')".format(rollno,name,dob,gender)
 CMD.execute(Q)
 CN.commit()
 print("Record Submitted")
 CN.close()
except Exception as e:
    print(e)
