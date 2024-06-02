from flask import Flask, jsonify
from config import Config
from controllers.delete_event_controller import DeleteEventController
from controllers.get_event_controller import GetEventController
from controllers.get_events_controller import GetEventsController
from controllers.join_event_controller import JoinEventController
from controllers.leave_event_controller import LeaveEventController
from controllers.sports_controller import SportsController
from models import db
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from controllers.create_event_controller import CreateEventController
from controllers.register_controller import RegisterController
from controllers.login_controller import LoginController
from controllers.get_categories_controller import GetCategoriesController
from controllers.is_participant_controller import IsParticipantController
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://drda64.github.io"}})

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
app.add_url_rule('/event/<string:event_id>', view_func=GetEventController.as_view('event'))
app.add_url_rule('/category/<string:event_id>', view_func=GetCategoriesController.as_view('category'))
app.add_url_rule('/join_event/<string:event_id>', view_func=JoinEventController.as_view('join_event'))
app.add_url_rule('/is_participant/<string:event_id>', view_func=IsParticipantController.as_view('is_participant'))
app.add_url_rule('/leave_event/<string:event_id>', view_func=LeaveEventController.as_view('leave_event'))
app.add_url_rule('/delete_event/<string:event_id>', view_func=DeleteEventController.as_view('delete_event'))


if __name__ == '__main__':
    app.run(debug=True, port=6555)
