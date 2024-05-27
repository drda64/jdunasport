from models.user import User
from flask import request, jsonify
from flask.views import MethodView
from schemas.register_schema import RegisterSchema
from werkzeug.security import generate_password_hash
from models import db
from marshmallow.exceptions import ValidationError


class RegisterController(MethodView):
    def post(self):
        schema = RegisterSchema()

        try:
            data = schema.load(request.get_json())
        except ValidationError as e:
            return jsonify(e.messages), 400

        user = User(
            username=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password'])
        )

        db.session.add(user)
        db.session.commit()
        return jsonify({
            'message': 'User created successfully'
        })
