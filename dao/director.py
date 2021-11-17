from flask import request
from sqlalchemy import desc

from dao.model.director import Directors


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Directors).all()

    def get_one(self, did):
        return self.session.query(Directors).get(did)
