from app import db
from datetime import datetime


class Prediction(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email_text = db.Column(
        db.Text,
        nullable=False
    )

    prediction_result = db.Column(
        db.String(100),
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )