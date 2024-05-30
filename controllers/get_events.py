from flask.views import MethodView
from flask import request, jsonify
from models.event import Event


class GetEventsController(MethodView):
    def get(self):
        events = Event.query.all()
        return jsonify(Event.serialize(events))
