from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from models import db, Person

user = Blueprint('user', __name__)
api = Api(user)




class UserResource(Resource):
    def post(self):
        data = request.get_json()
        user = Person(name=data['name'], age=data['age'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize()), 201

    def put(self, user_id):
        user = Person.query.get(user_id)
        if user:
            data = request.get_json()
            user.name = data['name']
            user.age = data['age']
            db.session.commit()
            return jsonify(user.serialize())
        else:
            return jsonify({'message': 'User not found'}), 404

    def delete(self, user_id):
        user = Person.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted'})
        else:
            return jsonify({'message': 'User not found'}), 404

    def get(self, user_id):
        user = Person.query.get(user_id)
        if user:
            return jsonify(user.serialize())
        else:
            return jsonify({'message': 'User not found'}), 404



api.add_resource(UserResource, '/user', '/user/<int:user_id>')



