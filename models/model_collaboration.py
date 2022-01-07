from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, ForeignKey, Column, String
from app import db


class Collaboration_Model(db.Model):
    supply_id = db.Column(db.String, primary_key=True)
    comments = db.Column(JSONB)
    feedback = db.Column(JSONB)
    demand_id = db.Column(db.String, nullable=True)
    is_hide = db.Column(db.Boolean)
    add_members = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Collaboration {}>'.format(self.comments)
