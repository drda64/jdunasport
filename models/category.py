from . import db
from datetime import datetime
from .base_model import BaseModel
from .participant import Participant

class Category(BaseModel):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    event = db.relationship('Event', backref=db.backref('categories', lazy=True))

    def to_dict(self):
        # we get the parcipants of the category
        participants = Participant.query.filter_by(category_id=self.id).all()

        return {
            'id': self.id,
            'event_id': self.event_id,
            'name': self.name,
            'capacity': self.capacity,
            'participants': Participant.serialize(participants),
            'created_at': self.created_at
        }

    def is_full(self, event_id, category_id):
        # we query the participants, that are not substitutes
        participants = Participant.query.filter_by(event_id=event_id, category_id=category_id, substitute=0).all()

        if len(participants) >= self.capacity:
            return True

        return False

    def update_subs(self):
        # we query the participants, that are not substitutes
        participants = Participant.query.filter_by(category_id=self.id, substitute=0).all()

        if len(participants) >= self.capacity:
            # we query the participants, that are substitutes and order them by the time they joined the event
            participants = Participant.query.filter_by(category_id=self.id, substitute=1).order_by(Participant.created_at).all()

            # we update the as many participants as the capacity of the category
            for participant in participants:
                participant.substitute = 0
                participant.save()