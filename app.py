from flask import Flask
from config import Config
from models import db
from flask_jwt_extended import JWTManager
from controllers.create_event_controller import CreateEventController
from controllers.register_controller import RegisterController
from controllers.login_controller import LoginController

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
