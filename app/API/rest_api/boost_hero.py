
from flask import request
from flask_restplus import Resource
from Models import *
from dashboard import api, redis_store
from API.dataModel import boost_hero_model

ns = api.namespace('/')

@ns.route('/boost_hero')
class Boost_Hero(Resource):

    @api.expect(boost_hero_model)
    def post(self):

        data = request.json
        session_id = data['session_id']
        hero_id = data['hero_id']

        hero_id = str(hero_id)
        username = redis_store.get_item(session_id)
        if not username:
            return ({'Status' : 'please login'})
        username = username.decode('utf-8')

        if not username:
            return ({'Status': 'please login'})


        hero = Player_Hero.boost_energy(username, hero_id)

        if hero:
            return ({'Status' : ' Hero Charged'}), 200
        else:
            return ({'Status' : ' Not Found'})
