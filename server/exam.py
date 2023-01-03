import json
from flask import request, jsonify
from flask_restx import Resource, Namespace
import databases

Exam = Namespace(
    name='Exam',
    description="토익 테스트 관련 API"
)

@Exam.route('')
class ExamPost(Resource):
    def __init__(self, cusur) :
        self.cusur = databases.db_conn()
        self.db = databases.db

    def get(self):
        """토익 문제를 랜덤으로 불러옵니다."""
        result = {}

        #단어
        sql = 'select word, mean from word order by rand() limit 0,5;'
        self.cusur.execute(sql)
        result['word'] = self.cusur.fetchall()

        #숙어
        sql = 'select idiom, mean from idiom order by rand() limit 0,5;'
        self.cusur.execute(sql)
        result['idiom'] = self.cusur.fetchall()

        return jsonify(result)


# @Exam.route('/<int:id>')
# @Exam.doc(params={'id': 'seq'})
# @Exam.doc(responses={202: 'Success'})
# @Exam.doc(responses={500: 'Failed'})
# class ExamAPI(Resource):
#     def __init__(self, cusur) :
#         self.cusur = databases.db_conn()
#         self.db = databases.db


#     def get(self, id):
#         """특정 토익 숙어를 불러옵니다"""
#         sql = 'select * from idiom where seq='+str(id)+';'
#         self.cusur.execute(sql)
#         result = self.cusur.fetchall()
#         return jsonify(result)
        

#     def put(self, id):
#         """특정 토익 숙어를 업데이트 합니다"""
#         data = request.form.to_dict()
#         data = next(iter(data))
#         data = json.loads(data)

#         idiom = data.get('idiom')
#         mean = data.get('mean')

#         sql = "update idiom set idiom='%s', mean='%s'"%(idiom, mean) + "where seq="+str(id)+";"

#         self.cusur.execute(sql)
#         self.db.commit()

#         return {
#             "result" : "success"
#         }

    
#     def delete(self, id):
#         """특정 토익 숙어를 삭제 합니다"""
#         sql = "delete from idiom where seq="+str(id)+";"
#         self.cusur.execute(sql)
#         self.db.commit()
        
#         return {
#             "result" : "success"
#         }