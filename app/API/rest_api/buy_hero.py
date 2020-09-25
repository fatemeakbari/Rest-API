
from flask import request
from flask_restplus import Resource
from dashboard import redis_store, api, db
from Models import *
from API.dataModel import buy_hero_model


ns = api.namespace('/')

@ns.route('/buyHero')
class BuyHero(Resource):

    @api.expect(buy_hero_model)
    def post(self):
        """
        buy hero
        """
        data = request.json
        session_id = data['session_id']
        hero_id = data['hero_id']

        hero_id = str(hero_id)
        username = redis_store.get_item(session_id)


        if not username:
            return ({'Status' : 'Please Login'})
        username = username.decode('utf-8')

        hero = Hero.get_hero_by_heroID(hero_id)
        if not hero:
            return ({'Status' : 'Hero Not Found'})


        user = User.get_user_by_username(username)
        if not User.check_coin(user.coin, hero.price):
            return ({'Status' : 'Coin Not Enough'})

        if not User.check_level(user.level, hero.minimumRequiredLevel):
            return ({'Status' : 'Level Is Low'})

        if  Player_Hero.get_exist_playerHero(username, hero_id) != None:
            return ({'Status' : 'Hero Already Selected'})



        new_player_hero = Player_Hero(hero.hero_id, hero.energy, hero.recovery_rate, username)
        player_hero = new_player_hero.save_to_db()

        user.update_coin(-hero.price)
        user.update_db()

        if player_hero:

            return ({'Status': 'The Hero Received Successfuly', 'hero_id' : hero.hero_id, 'session_id':session_id}), 200
        else:
            return ({'Status': 'Not Found'})
