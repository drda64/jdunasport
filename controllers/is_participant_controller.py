from flask.views import MethodView

from flask import request, jsonify

from models.participant import Participant
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User


class IsParticipantController(MethodView):
    @jwt_required()
    def get(self, event_id):
        user_id = get_jwt_identity()
        participant = Participant.query.filter_by(event_id=event_id, user_id=user_id).first()
        if participant:
            user = User.query.filter_by(id=user_id).first()
            return jsonify({'username': user.username, 'category_id': participant.category_id}), 200
        return jsonify({'username':''}), 200
