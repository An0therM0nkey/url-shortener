import random
import string
from datetime import datetime

from sqlalchemy_serializer import SerializerMixin

from .db import db


CHARACTERS = string.ascii_letters + string.digits  # 26 + 26 + 10 = 62
AMOUNT = 5  # enough for (62! / (5! * (62 - 5)!)) = 6471002 possible combinations


class LinksPair(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024))
    short_url = db.Column(db.String(AMOUNT))
    date_created = db.Column(db.DateTime, default=datetime.now())
    days_limit = db.Column(db.Integer, default=90)

    __table_args__ = (
        db.CheckConstraint('days_limit >= 1 AND days_limit <= 365'),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        while True:
            short_url = ''.join(random.choice(CHARACTERS) for i in range(AMOUNT))
            if not self.query.filter_by(short_url=short_url).first():
                return short_url
