from flask_restplus import Resource
from flask import request
import hashlib
from Models import *
from dashboard import redis_store, api
from API.dataModel import startGame_model2



ns = api.namespace('/')

@ns.route('/startGame')
class startGame(Resource):

    @api.expect(startGame_model2)
    def post(self):

        """
        start game
        """

        # get info from user
        data = request.json
        hero1 = data['hero1']
        hero2 = data['hero2']
        hero3 = data['hero3']
        session_id = data['session_id']

        hero1 = str(hero1)
        hero2 = str(hero2)
        hero3 = str(hero3)
        username = redis_store.get_item(session_id)
        if not username:
            return ({'Status': 'Please Login'})
        username = username.decode('utf-8')

        active_hero = Player_Hero.start_game(username, hero1, hero2, hero3)
        if active_hero != None:
            return active_hero
        return ({'Status': 'Try Again'})
        '''
        nickname1 = User.get_nickname_by_username(username1)
        nickname2 = User.get_nickname_by_username(username2)

        if nickname1 == None:
                return ({'Status':username1 + ' not found'})
        if nickname2 == None:
                return ({'Status':username2 + ' not found'})

        hero_list1 = Player_Hero.get_active_playerHero(username1)
        hero_list2 = Player_Hero.get_active_playerHero(username2)

        if hero_list1 == None or hero_list2 == None:
            return ({'Status' : 'Not Found'})
        return ( { username1:{'nickname' : nickname1, 'heros' : hero_list1}, username2:{'nickname' : nickname2, 'heros' :hero_list2}})
        '''
