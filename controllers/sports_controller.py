from flask.views import MethodView
from flask import request, jsonify
from models.sport import Sport


class SportsController(MethodView):
    def get(self):
        sports = Sport.getAll()
        return jsonify(Sport.serialize(sports))
