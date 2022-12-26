import pymysql

db = pymysql.connect(
        user='root', 
        passwd='rhdqn.', 
        host='127.0.0.1', 
        db='toeic', 
        charset='utf8'
    )

def db_conn():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return cursor

# sql = "SELECT * FROM word;"
# cursor.execute(sql)
# result = cursor.fetchall()

# print(result)


