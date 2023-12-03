from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from models import db, Person

user = Blueprint('user', __name__)
api = Api(user)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('firstname', type=str, required=True)
parser.add_argument('lastname', type=str, required=True)

class UserResource(Resource):
    def get(self, user_id):
        user = Person.query.get(user_id)
        if user:
            return jsonify(user.serialize())
        return jsonify({'message': 'User not found'})
        
    def post(self):
        args = parser.parse_args(strict=True)
        user = Person(**args)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize())



api.add_resource(UserResource, '/user', '/user/<int:user_id>')

