from . import db
from datetime import datetime
from .user import User
from .sport import Sport
from .base_model import BaseModel


class Event(BaseModel):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sports.id'), nullable=False)
    location = db.Column(db.String(100))
    event_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('events', lazy=True))
    sport = db.relationship('Sport', backref=db.backref('events', lazy=True))

    def to_dict(self):
        # zistime sport, ktery ma id sport_id
        sport = Sport.getFirst(id=self.sport_id)
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'sport': sport.name,
            'location': self.location,
            'event_time': self.event_time.isoformat(),
            'created_at': self.created_at.isoformat()
        }
