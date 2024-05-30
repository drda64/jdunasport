from flask import Flask, jsonify
from config import Config
from controllers.get_event_controller import GetEventController
from controllers.get_events import GetEventsController
from controllers.join_event_controller import JoinEventController
from controllers.sports_controller import SportsController
from models import db
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from controllers.create_event_controller import CreateEventController
from controllers.register_controller import RegisterController
from controllers.login_controller import LoginController
from controllers.get_categories_controller import GetCategoriesController

app = Flask(__name__)

# nakonfigurujeme z objektu Config
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

# zaregistrujeme blueprints
app.add_url_rule('/create_event', view_func=CreateEventController.as_view('create_event'))
app.add_url_rule('/register', view_func=RegisterController.as_view('register'))
app.add_url_rule('/login', view_func=LoginController.as_view('login'))
app.add_url_rule('/sports', view_func=SportsController.as_view('sports'))
app.add_url_rule('/events', view_func=GetEventsController.as_view('events'))
app.add_url_rule('/event/<int:event_id>', view_func=GetEventController.as_view('event'))
app.add_url_rule('/category/<int:event_id>', view_func=GetCategoriesController.as_view('category'))
app.add_url_rule('/join_event/<int:event_id>', view_func=JoinEventController.as_view('join_event'))


@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    return {"access_token": new_token}, 200


if __name__ == '__main__':
    app.run(debug=True, port=6555)
