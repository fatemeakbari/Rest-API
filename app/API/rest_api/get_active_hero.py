
from flask import request
from flask_restplus import Resource
from dashboard import redis_store, api, db
from Models import *



ns = api.namespace('/')

@ns.route('/getActiveHero/<session_id>')
class GetActiveHero(Resource):


    def get(self, session_id):
        """
        get active hero
        """
        username = redis_store.get_item(session_id)
        if not username:
            return ({'Status' : 'Please Login'})
        username = username.decode('utf-8')

        activeHero = Player_Hero.get_active_playerHero(username)
        if activeHero != None:
            return ({'active heros' : activeHero, 'session_id':session_id})
        return ({'Status': 'Not Found', 'session_id':session_id})
