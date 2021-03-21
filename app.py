from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

array = []
class Fight(Resource):
    def get(self):
        print(request.get_json())
        return 1



api.add_resource(Fight, '/fight/')


