from flask import request, jsonify
from flask_restx import Resource, Namespace
import databases

Idiom = Namespace(
    name='Idiom',
    description="토익 숙어 CRUD 관련 API"
)

@Idiom.route('')
class IdiomPost(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()
        self.db = databases.db

    def get(self):
        """모든 토익 숙어를 불러옵니다."""
        sql = 'select * from idiom;'
        self.cusur.execute(sql)
        result = self.cusur.fetchall()
        return jsonify(result)
  
    def post(self):
        """토익 숙어를 추가합니다."""
        idiom = request.form.get('idiom')
        mean = request.form.get('mean')

        sql = "INSERT INTO idiom (idiom, mean) VALUES ('%s', '%s');" %(idiom, mean) 
        self.cusur.execute(sql)
        self.db.commit()

        return {
            "result" : "success"
        }


@Idiom.route('/<int:id>')
@Idiom.doc(params={'id': 'seq'})
@Idiom.doc(responses={202: 'Success'})
@Idiom.doc(responses={500: 'Failed'})
class IdiomAPI(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()
        self.db = databases.db


    def get(self, id):
        """특정 토익 숙어를 불러옵니다"""
        sql = 'select * from idiom where seq='+str(id)+';'
        self.cusur.execute(sql)
        result = self.cusur.fetchall()
        return jsonify(result)
        

    def put(self, id):
        """특정 토익 숙어를 업데이트 합니다"""
        idiom = request.form.get('idiom')
        mean = request.form.get('mean')

        sql = "update idiom set idiom='%s', mean='%s'"%(idiom, mean) + "where seq="+str(id)+";"

        self.cusur.execute(sql)
        self.db.commit()

        return {
            "result" : "success"
        }

    
    def delete(self, id):
        """특정 토익 숙어를 삭제 합니다"""
        sql = "delete from idiom where seq="+str(id)+";"
        self.cusur.execute(sql)
        self.db.commit()
        
        return {
            "result" : "success"
        }