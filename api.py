from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Elvis",
        "age": 43,
        "occupation": "Network Engineer"
    },
    {
        "name": "Nick",
        "age": 62,
        "occupation": "Doctor"
    },
    {
        "name": "Jess",
        "age": 29,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

   
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
