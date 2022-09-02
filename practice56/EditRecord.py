import pymysql as MySql
try:
 CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123',database="studentmanagement")
 #CN is an object which contains address of Database Engine
 CMD=CN.cursor()
 #CMD is an Object use to supply query to Database Engine
 rollno=input("Enter Rollno:")
 name=input("Enter New Name:")
 Q="update student set studentname='{0}' where rollno='{1}'".format(name,rollno)
 CMD.execute(Q)
 CN.commit()
 print("Record Updated Succesfully")
 CN.close()
except Exception as e:
    print(e)
