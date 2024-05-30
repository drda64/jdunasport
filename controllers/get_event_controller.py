from flask.views import MethodView

from flask import request, jsonify

from models.event import Event

class GetEventController(MethodView):
    def get(self, event_id):
        event = Event.getFirst(id=event_id)
        return jsonify(Event.to_dict(event))