from . import db
from datetime import datetime
from .base_model import BaseModel


class Sport(BaseModel):
    __tablename__ = 'sports'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat()  # Convert datetime to ISO format string
        }
