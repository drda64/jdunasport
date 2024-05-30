import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.urandom(32).hex()
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/jdunasport"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "letsgoooo"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)