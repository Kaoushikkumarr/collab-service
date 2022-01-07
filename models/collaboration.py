from sqlalchemy.dialects.postgresql import JSONB

from app import db


class Collaboration(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	comments = db.Column(JSONB)
	feedbacks = db.Column(JSONB)
	tasks = db.Column(JSONB)
	interviews = db.Column(JSONB)
	activities = db.Column(JSONB)
	supply_id = db.Column(db.Integer, nullable=True)

	def __repr__(self):
		return '<Collaboration {}>'.format(self.comments)
