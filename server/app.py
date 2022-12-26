from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
import json
from flask_restx import Api, Resource, Namespace
from word import Word
from idiom import IdiomResource
import databases


# configuration

# instantiate the app
app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_namespace(Word, '/word')
api.add_namespace(IdiomResource, '/idiom')

# enable CORS
#CORS(app, resources={r'/*': {'origins': '*'}})


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {"hello": "world!"}

# @app.route('/volt', methods=['GET', 'POST'])
# def all_books():
#     response_object = {'status': 'success'}
#     cursor = sphere.cursor(pymysql.cursors.DictCursor)

#     if request.method == 'POST':
#         # post_data = request.get_json()
#         # BOOKS.append({
#         #     'id': uuid.uuid4().hex,
#         #     'title': post_data.get('title'),
#         #     'author': post_data.get('author'),
#         #     'read': post_data.get('read')
#         # })


#         response_object['message'] = 'Book added!'
#     else:
#         sql = "SELECT count(*) FROM volt;"

#         sql = "SELECT * FROM volt;"
#         cursor.execute(sql)
#         response_object['volt'] = cursor.fetchall()
#     return jsonify(response_object)

# test data
# curl -X POST http://127.0.0.1:5000/books -d '{"title": "1Q84", "author": "Haruki Murakami", "read": "true"}' -H 'Content-Type: application/json

# @app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
# def single_book(book_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book updated!'
#     if request.method == 'DELETE':
#         remove_book(book_id)
#         response_object['message'] = 'Book removed!'
#     return jsonify(response_object)

# def remove_book(book_id):
#     for book in BOOKS:
#         if book['id'] == book_id:
#             BOOKS.remove(book)
#             return True
#     return False

if __name__ == '__main__':
    app.run(debug=True)
    
