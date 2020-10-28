import random
import string
from datetime import datetime

from sqlalchemy_serializer import SerializerMixin

from .db import db


class LinksPair(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024))
    short_url = db.Column(db.String(64))
    date_created = db.Column(db.DateTime, default=datetime.now())
    days_limit = db.Column(db.Integer, default=90)

    __table_args__ = (
        db.CheckConstraint('days_limit >= 1 AND days_limit <= 365'),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for i in range(8))
            if not self.query.filter_by(short_url=short_url).first():
                return short_url
