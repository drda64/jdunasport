import os
from datetime import timedelta


class Config:
    SECRET_KEY = "bro"
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://Drda64:Drda2003@Drda64.mysql.pythonanywhere-services.com/Drda64$jdunasport"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "letsgoooo"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    CORS_HEADERS = 'Content-Type'