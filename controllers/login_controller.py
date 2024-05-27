from flask.views import MethodView
from flask import request, jsonify
from werkzeug.security import check_password_hash
from models import db
from models.user import User
from flask_jwt_extended import create_access_token
from schemas.login_schema import LoginSchema
from marshmallow.exceptions import ValidationError


class LoginController(MethodView):
    def post(self):
        schema = LoginSchema()

        try:
            data = schema.load(request.get_json())
        except ValidationError as e:
            return jsonify(e.messages), 400

        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return jsonify({'message': 'Login successful!', 'access_token': create_access_token(identity=username)})

        return jsonify({'message': 'Invalid credentials!'}), 401
