from . import db
from datetime import datetime
from .base_model import BaseModel

class Participant(BaseModel):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    substitute = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    event = db.relationship('Event', backref=db.backref('participants', lazy=True))
    user = db.relationship('User', backref=db.backref('participants', lazy=True))
    category = db.relationship('Category', backref=db.backref('participants', lazy=True))

    def to_dict(self):
        # username
        username = self.user.username
        print(self.substitute)
        return {
            'id': self.id,
            'username': username,
            'substitute': self.substitute,
            'created_at': self.created_at
        }