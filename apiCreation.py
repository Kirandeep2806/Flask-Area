from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("fname", type=str, help="First name is required", required=True, location="args")
parser.add_argument("lname", type=str, help="Enter the last name", location="args")
parser.add_argument("age", type=int, help="Age is required", required=True, location="args")
parser.add_argument("male", type=bool, help="Gender is required", required=True, location="args")

data = {"kiran": {"name": {"fname": "Kiran", "lname": "Deep"}, "age": 18, "male": True},
        "dileep": {"name": {"fname": "Dileep", "lname": "Sai"}, "age": 21, "male": True}}

class Print(Resource):
    def get(self, name):
        if name not in data:
            abort(404, message="Name don't exist!")
        return data[name], 200
    
    def put(self, name):
        if name in data:
            abort(409, message="Data already exists!")
        args = parser.parse_args()
        data[name] = {"name": {"fname" : args["fname"], "lname": args["lname"]}, "age": args["age"], "male": args["male"]}
        return data, 201
    
    def delete(self, name):
        if name not in data:
            abort(404, message="Name don't exist!")
        del data[name]
        return '', 204

api.add_resource(Print, "/print/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
