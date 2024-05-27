from marshmallow import Schema, fields, validates, ValidationError
from models.user import User


class RegisterSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @validates('username')
    def validate_username(self, value):
        #zkontrolujeme, zda jiz neni v databazi
        user = User.query.filter_by(username=value).first()

        if user:
            raise ValidationError("User already exists")

    @validates('password')
    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError('Password must be at least 6 characters long')

    @validates('email')
    def validate_email(self, value):
        user = User.query.filter_by(email=value).first()

        if user:
            raise ValidationError("Email already exists")
