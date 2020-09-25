from Models import *
from flask_restplus import Resource
from dashboard import redis_store, api


ns = api.namespace('/')

@ns.route('/getCoin/<session_id>')

class GetCoin(Resource):

    def get(self, session_id):

        username = redis_store.get_item(session_id)
        if not username:
            return ({'Status' : 'please login'})
        username = username.decode('utf-8')

        coin = User.get_coin(username)
        if coin:
            return ({"user's coin" : int(coin), 'session_id': session_id}), 200
        return ({'Status' : 'Not Found'})
