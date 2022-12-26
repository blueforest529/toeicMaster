from flask import request
from flask_restx import Resource, Api, Namespace
# from db_connector import DBConnector

IdiomResource = Namespace('IdiomResource')

@IdiomResource.route('')
class RequestDAO(Resource):
    def get(self):
        # DBc = DBConnector()
        # result = DBc.select('resource_req')
        
        # return result
        return ''
        
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