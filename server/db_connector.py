import pymysql
import json

sphere = pymysql.connect(
    user='root', 
    passwd='rhdqn.', 
    host='127.0.0.1', 
    db='sphere', 
    charset='utf8'
)

class DBConnector:
    def __init__(self):
        self.cursor = sphere.cursor(pymysql.cursors.DictCursor)

    def select(self, table):
        sql = "select * from "+ table
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result = json.dumps(result, default=str)

        return result
    

# def main():
#     DBc = DBConnector()
#     print(DBc.select('request'))

    
# if __name__ == "__main__":
#     main()


