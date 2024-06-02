from flask.views import MethodView

from flask import request, jsonify

from models.category import Category
from models.event import Event


class GetCategoriesController(MethodView):
    def get(self, event_id):
        # we check if the event exists
        event = Event.getFirst(id=event_id)

        if not event:
            return jsonify({'message': 'Event not found'}), 404

        categories = Category.query.filter_by(event_id=event_id).all()
        return jsonify(Category.serialize(categories))
