

import json

from flask import jsonify, request
from flask_restx import Namespace, Resource
from sqlalchemy import desc

from setup_db import db
from implemented import movie_service
from dao.model.movie import usefull_many,usefull_one
# from models import Movies, usefull_many, usefull_one
# from models import Movies, Genres, Directors

movies_ns = Namespace('movies')


@movies_ns.route('/')
class Movies_view(Resource):
    def get(self):
        all_movies = movie_service.get_all_movies()
        return jsonify(usefull_many.dump(all_movies))

@movies_ns.route('/<int:mid>')
class Movie_view(Resource):
    def get(self,mid):
        one_movie = movie_service.get_one_movie(mid)
        return jsonify(usefull_many.dump(one_movie))

    def put(self,mid):
        movie_details = request.json
        mov = movie_service.update_movie(mid, movie_details)
        return "updated", 201

    def delete(self,mid):
        mov = movie_service.delete_movie(mid)
        return "deleted", 204