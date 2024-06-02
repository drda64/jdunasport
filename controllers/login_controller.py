from flask.views import MethodView
from flask import request, jsonify
from werkzeug.security import check_password_hash
from models import db
from models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token
from schemas.login_schema import LoginSchema
from marshmallow.exceptions import ValidationError
from services.password_hasher import check_password


class LoginController(MethodView):
    def post(self):
        schema = LoginSchema()

        try:
            data = schema.load(request.get_json())
        except ValidationError as e:
            return jsonify(e.messages), 400

        username = data.get('username')
        password = data.get('password')

        user = User.getFirst(username=username)

        if user and check_password(user.password, password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return jsonify({'message': 'Přihlášení bylo úspěšné!', 'access_token': access_token, 'refresh_token': refresh_token})

        return jsonify({'message': 'Neplatné přihlašovací údaje'}), 401
