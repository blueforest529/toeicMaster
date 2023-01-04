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
        sql = 'select idiom as word, mean from idiom order by rand() limit 0,5;'
        self.cusur.execute(sql)
        result['idiom'] = self.cusur.fetchall()

        return jsonify(result)

