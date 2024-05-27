from flask.views import MethodView
from flask import request, jsonify
from models.event import Event
from flask_jwt_extended import jwt_required


class CreateEventController(MethodView):
    @jwt_required()
    def post(self):
        data = request.get_json()
        event = Event(
            name=data['name'],
            date=data['date'],
            description=data['description'],
            location=data['location']
        )
        event.save()
        return jsonify({
            'message': 'Event created successfully'
        })
