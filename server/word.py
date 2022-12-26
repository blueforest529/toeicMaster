from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
import databases

Word = Namespace('Word')
@Word.route('')
class WordPost(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()
        self.db = databases.db

    def get(self):
        sql = 'select * from word;'
        self.cusur.execute(sql)
        result = self.cusur.fetchall()
        return jsonify(result)
  
    def post(self):
        # return {"hello": "world!"}
        word = request.json.get('word')
        parts = request.json.get('parts')
        mean = request.json.get('mean')

        sql = "INSERT INTO word (word, parts, mean) VALUES ('%s', '%s', '%s');" %(word, parts, mean) 
        self.cusur.execute(sql)
        self.db.commit()
        
        return {
            "result" : "success"
        }

        


@Word.route('/<int:id>')
class WordAPI(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()

    def get(self, id):
        sql = 'select * from word where seq='+str(id)+';'
        self.cusur.execute(sql)
        result = self.cusur.fetchall()
    
        return jsonify(result)

        
    def put(self, id):
        return {
            
        }

    
    def delete(self, ids):
        return {
            

        }


        


