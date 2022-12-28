from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource
from word import Word
from idiom import Idiom

app = Flask(__name__)
CORS(app)
#보안 상의 이유로 자원에 대한 접근을 브라우저가 제한하는 경우를 방지
api = Api(
    app,
    version='0.1',
    title="Cheong's API Server",
    description="Cheong's Toeic study API Server!",
    terms_url="/",
    contact="blueforest529@gmail.com",
    license="MIT"
)

api.add_namespace(Word, '/word')
api.add_namespace(Idiom, '/idiom')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        """API의 health check를 담당합니다"""
        return {"hello": "world!"}

if __name__ == '__main__':
    app.run(debug=True)
    
