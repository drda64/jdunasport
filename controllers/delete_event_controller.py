from flask.views import MethodView

from flask import request, jsonify

from models.event import Event

from flask_jwt_extended import get_jwt_identity, jwt_required

class DeleteEventController(MethodView):
    @jwt_required()
    def delete(self, event_id):
        # get the user_id from the jwt token
        user_id = get_jwt_identity()

        # check if the event exists
        event = Event.getFirst(id=event_id)

        # if event is None, return 404
        if not event:
            return jsonify({'message': 'Event not found'}), 404

        # check if created by this user
        if event.user_id != user_id:
            return jsonify({'message': 'Unauthorized'}), 401

        # delete the event
        event.delete(id=event_id)

        return jsonify({'message': 'Event deleted'}), 200