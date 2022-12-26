from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
# from db_connector import DBConnector

VoltResource = Namespace('VoltResource')

@VoltResource.route('')
class RequestDAO(Resource):
    def get(self):
        # response_object = {'status': 'success'}

        # DBc = DBConnector()
        # response_object['volt']  = DBc.select('volt')

        return ''
        # return jsonify(response_object)
        
        
    def put(self):
        return {
            # null
        }
    
    def post(self):
        return {
            
        }
    
    def delete(self):
        return {
            

        }