

import json

from flask import jsonify, request
from flask_restx import Namespace, Resource
from sqlalchemy import desc

from setup_db import db
from implemented import director_service
from dao.model.movie import usefull_many,usefull_one
# from models import Movies, usefull_many, usefull_one
# from models import Movies, Genres, Directors

directors_ns = Namespace('directors')


@directors_ns.route('/')
class Directors_view(Resource):
    def get(self):
        all_directors = director_service.get_all_directors()
        return jsonify(usefull_many.dump(all_directors))

@directors_ns.route('/<int:did>')
class Director_view(Resource):
    def get(self,did):
        one_director = director_service.get_one_director(did)
        return jsonify(usefull_one.dump(one_director))