import math
from flask.views import MethodView
from flask import request, jsonify
from models.event import Event
from models.participant import Participant
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import or_, and_

class GetEventsController(MethodView):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        history = request.args.get('history')
        date_up = request.args.get('date_up')
        page = int(request.args.get('page', 1))
        per_page = 10

        today = datetime.today().date()
        start_of_the_day = datetime.combine(today, datetime.min.time())

        # Determine the ordering based on date_up parameter
        if date_up == 'true':
            time_arg = Event.event_time
        else:
            time_arg = Event.event_time.desc()

        # Determine the filtering based on history parameter
        if history == 'false':
            hist_arg = Event.event_time > start_of_the_day
        else:
            hist_arg = Event.event_time < start_of_the_day

        # Calculate the offset
        offset_value = (page - 1) * per_page

        # Query the total count of events matching the criteria and involving the user
        total_events = (Event.query
                        .join(Participant, and_(Participant.event_id == Event.id, Participant.user_id == user_id), isouter=True)
                        .filter(hist_arg)
                        .filter(or_(Event.user_id == user_id, Participant.user_id == user_id)))

        max_pages = math.ceil(total_events.count() / per_page)

        # Query the events with the correct filter, ordering, offset, and limit
        events = (Event.query
                  .join(Participant, and_(Participant.event_id == Event.id, Participant.user_id == user_id), isouter=True)
                  .filter(hist_arg)
                  .filter(or_(Event.user_id == user_id, Participant.user_id == user_id))
                  .order_by(time_arg)
                  .offset(offset_value)
                  .limit(per_page)
                  .all())

        for event in total_events:
            print(event.id)

        print(total_events.count())

        response_data = {
            'events': Event.serialize(events, user_id),
            'total_pages': max_pages,
            'current_page': page
        }

        return jsonify(response_data)
