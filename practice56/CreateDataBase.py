import pymysql as MySql

CN=MySql.connect(host='localhost',port=3306,user='root',passwd='123')
#CN is an object which contains address of Database Engine
CMD=CN.cursor()
#CMD is an Object use to supply query to Database Engine
Q="Create Database StudentManagement"
CMD.execute(Q)
CN.commit()
print("Database Created")
CN.close()


