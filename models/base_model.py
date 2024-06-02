import random
import string

from models import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getFirst(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def checkIfAlreadyExists(cls, **kwargs):
        if cls.query.filter_by(**kwargs).first():
            return True

        return False

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def delete(cls, **kwargs):
        cls.query.filter_by(**kwargs).delete()
        db.session.commit()

    @classmethod
    def serialize(cls, data):
        return [item.to_dict() for item in data]

    @classmethod
    def generate_unique_code(cls):
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            if not cls.query.get(code):
                return code

