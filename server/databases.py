import pymysql

sphere = pymysql.connect(
    user='root', 
    passwd='rhdqn.', 
    host='127.0.0.1', 
    db='sphere', 
    charset='utf8'
)

cursor = sphere.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM volt;"
cursor.execute(sql)
result = cursor.fetchall()

print(result)


