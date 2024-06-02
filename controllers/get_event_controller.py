from flask.views import MethodView

from flask import request, jsonify

from models.event import Event
from flask_jwt_extended import get_jwt_identity, jwt_required

class GetEventController(MethodView):
    @jwt_required()
    def get(self, event_id):
        event = Event.getFirst(id=event_id)

        if not event:
            return jsonify({'message': 'Event not found'}), 404

        return jsonify(Event.to_dict(event, get_jwt_identity()))