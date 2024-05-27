from flask import Flask
from config import Config
from models import db
from flask_jwt_extended import JWTManager
from controllers.create_event_controller import CreateEventController
from controllers.register_controller import RegisterController
from controllers.login_controller import LoginController

app = Flask(__name__)

# nakonfigurujeme z objektu Config
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

# zaregistrujeme blueprints
app.add_url_rule('/create_event', view_func=CreateEventController.as_view('create_event'))
app.add_url_rule('/register', view_func=RegisterController.as_view('register'))
app.add_url_rule('/login', view_func=LoginController.as_view('login'))

if __name__ == '__main__':
    app.run()
