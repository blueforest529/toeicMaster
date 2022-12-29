import json
from flask import request, jsonify
from flask_restx import Resource, Namespace
import databases

Word = Namespace(
    name='Word',
    description="토익 단어 CRUD 관련 API"
)

@Word.route('')
class WordPost(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()
        self.db = databases.db

    def get(self):
        """모든 토익 단어를 불러옵니다."""
        sql = 'select * from word;'
        self.cusur.execute(sql)
        result = self.cusur.fetchall()
        return jsonify(result)
  
    def post(self):
        """토익 단어를 추가합니다."""

        data = request.form.to_dict()
        data = next(iter(data))
        data = json.loads(data)

        word = data.get('word')
        parts = data.get('parts')
        mean = data.get('mean')

        print(word)

        sql = "INSERT INTO word (word, parts, mean) VALUES ('%s', '%s', '%s');" %(word, parts, mean) 
        self.cusur.execute(sql)
        self.db.commit()

        return {
            "result" : "success"
        }

@Word.route('/<int:id>')
@Word.doc(params={'id': 'seq'})
@Word.doc(responses={202: 'Success'})
@Word.doc(responses={500: 'Failed'})
class WordAPI(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()
        self.db = databases.db

    def get(self, id):
        """특정 토익 단어를 불러옵니다"""
        sql = 'select * from word where seq='+str(id)+';'
        self.cusur.execute(sql)
        result = self.cusur.fetchall()
        return jsonify(result)
        

    def put(self, id):
        """특정 토익 단어를 업데이트 합니다"""
        data = request.form.to_dict()
        data = next(iter(data))
        data = json.loads(data)

        word = data.get('word')
        parts = data.get('parts')
        mean = data.get('mean')

        sql = "update word set word='%s', parts='%s', mean='%s'"%(word, parts, mean) + "where seq="+str(id)+";"

        self.cusur.execute(sql)
        self.db.commit()

        return {
            "result" : "success"
        }

    
    def delete(self, id):
        """특정 토익 단어를 삭제 합니다"""
        sql = "delete from word where seq="+str(id)+";"

        self.cusur.execute(sql)
        self.db.commit()
        
        return {
            "result" : "success"
        }