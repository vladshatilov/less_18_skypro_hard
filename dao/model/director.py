from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from setup_db import db


class Directors(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))