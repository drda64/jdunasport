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

        print(user_id)
        print(category_id)

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

        # check if the category is full
        participants = Participant.query.filter_by(category_id=category_id).all()
        if len(participants) >= category.capacity:
            return jsonify({'message': 'Category is full'}), 400

        # else add the participant
        participant = Participant(event_id=event_id, user_id=user_id, category_id=category_id)
        participant.save()

        return jsonify({'message': 'Participant added'}), 200
