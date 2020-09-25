from flask_restplus import Resource
from flask import request
from dashboard import redis_store, api
from Models import *


ns = api.namespace('/')

@ns.route('/getAllHero/<session_id>')
class GetAllHero(Resource):


    def get(self, session_id):
        """
        get all heros
        """

        username = redis_store.get_item(session_id)

        if not username:
            return ({'Status' : 'Please Login'})
        username = username.decode("utf-8")

        #find nickname
        nickname = User.get_nickname_by_username(username)

        hero_list = Player_Hero.get_playerHero(username)

        if hero_list != None:
            return ({'nickname':nickname, 'hero' : hero_list, 'session_id': session_id}) ,200

        return ({'Status' : hero_list, 'session_id': session_id})
