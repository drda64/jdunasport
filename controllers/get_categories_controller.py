from flask.views import MethodView

from flask import request, jsonify

from models.category import Category


class GetCategoriesController(MethodView):
    def get(self, event_id):
        print(event_id)
        categories = Category.query.filter_by(event_id=event_id).all()
        return jsonify(Category.serialize(categories))
