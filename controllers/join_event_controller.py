from datetime import datetime

from flask.views import MethodView

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.participant import Participant
from models.event import Event
from models.category import Category


class JoinEventController(MethodView):
    @jwt_required()
    def post(self, event_id):
        # get the user_id from the jwt token
        user_id = get_jwt_identity()
        category_id = request.json.get('category_id')

        # Check if the event is older than today's 00:00
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        event = Event.query.get(event_id)
        if event.event_time < today_start:
            return jsonify({'message': 'Cannot join event that has already happened'}), 400

        # check if the user is already a participant
        participant = Participant.query.filter_by(event_id=event_id, user_id=user_id).first()

        if participant:
            return jsonify({'message': 'User is already a participant'}), 400

        # check if the event exists
        event = Event.query.get(event_id)
        if not event:
            return jsonify({'message': 'Event not found'}), 404

        # check if the category exists
        category = Category.query.get(category_id)
        if not category:
            return jsonify({'message': 'Category not found'}), 404

        substitute = 0

        # check if the category is full of not substitutes
        participants = Participant.query.filter_by(category_id=category_id, substitute=0).all()
        if len(participants) == category.capacity:
            substitute = 1

        # else add the participant
        participant = Participant(event_id=event_id, user_id=user_id, category_id=category_id, substitute=substitute)
        participant.save()

        return jsonify({'message': 'Participant added'}), 200
