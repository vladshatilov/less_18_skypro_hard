from flask_restx.fields import List

from dao.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.this_dao = dao

    def get_all_directors(self):
        return self.this_dao.get_all()

    def get_one_director(self,mid):
        return self.this_dao.get_one(mid)
