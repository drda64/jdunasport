from flask.views import MethodView
from flask import request, jsonify

from models.category import Category
from models.event import Event
from flask_jwt_extended import jwt_required, get_jwt_identity


class CreateEventController(MethodView):
    @jwt_required()
    def post(self):
        data = request.get_json()
        print(data)
        print(get_jwt_identity())

        event = Event()
        event.name = data['name']
        event.description = data['description']
        event.location = data['location']
        event.event_time = data['event_time']
        event.user_id = get_jwt_identity()
        event.sport_id = data['sport_id']
        event.save()

        # now we save the categories
        for category in data['categories']:
            category = Category(name=category["name"], event_id=event.id, capacity=category["capacity"])
            category.save()

        return "ok"
