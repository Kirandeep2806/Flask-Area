#!/usr/bin/python3

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

data = {"kiran": {"name": {"fname": "Kiran", "lname": "Deep"}, "age": 18, "male": True},
        "dileep": {"name": {"fname": "Dileep", "lname": "Sai"}, "age": 21, "male": True}}

class Print(Resource):
    def get(self, name):
        return data[name]

api.add_resource(Print, "/print/<string:name>", endpoint="print")


if __name__ == "__main__":
    app.run(debug=True)
