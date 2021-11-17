import json

from flask import jsonify, request
from flask_restx import Namespace, Resource
from sqlalchemy import desc

from setup_db import db
from implemented import genre_service
from dao.model.movie import usefull_many, usefull_one

# from models import Movies, usefull_many, usefull_one
# from models import Movies, Genres, Directors

genres_ns = Namespace('genres')


@genres_ns.route('/')
class Genres_view(Resource):
    def get(self):
        all_genres = genre_service.get_all_genres()
        return jsonify(usefull_many.dump(all_genres))


@genres_ns.route('/<int:gid>')
class Genre_view(Resource):
    def get(self, gid):
        one_genre = genre_service.get_one_genre(gid)
        return jsonify(usefull_one.dump(one_genre))
