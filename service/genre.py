from flask_restx.fields import List

from dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.this_dao = dao

    def get_all_genres(self):
        return self.this_dao.get_all()

    def get_one_genre(self,mid):
        return self.this_dao.get_one(mid)
