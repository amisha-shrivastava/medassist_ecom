import pymysql as MySQL


def ConnectionPooling():
    DB = MySQL.connect(host='localhost', port=3306, user='root', passwd='1510', database='medassist_com', cursorclass = MySQL.cursors.DictCursor)
    CMD = DB.cursor()
    return DB, CMD
