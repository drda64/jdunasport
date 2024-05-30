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