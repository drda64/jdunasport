from flask.views import MethodView

from flask import request, jsonify

from models.participant import Participant

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.category import Category


class LeaveEventController(MethodView):
    @jwt_required()
    def post(self, event_id):
        user_id = get_jwt_identity()
        participant = Participant.query.filter_by(event_id=event_id, user_id=user_id).first()

        if participant:
            category = Category.query.get(participant.category_id)
            category.update_subs()

            participant.delete(user_id=user_id, event_id=event_id)
            return jsonify({'message': 'You have left the event'}), 200
        return jsonify({'message': 'You are not a participant of this event'}), 400
