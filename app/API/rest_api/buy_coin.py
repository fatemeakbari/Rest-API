from flask_restplus import Resource
from flask import jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
from Models import *
from dashboard import redis_store, api
from API.dataModel import buyCoin_model



ns = api.namespace('/')

@ns.route('/buyCoin')
class BuyCoin(Resource):

    @api.expect(buyCoin_model)
    def post(self):

        """
        buy Coin
        """
        data = request.json
        session_id = data['session_id']
        numCoin = data['numCoin']


        username = redis_store.get_item(session_id)

        if not username:
            return ({'Status' : 'Please Login'})
        username = username.decode('utf-8')

        user = User.get_user_by_username(username)
        
        if user :
            user.update_coin(numCoin)
            user.update_db()
            return ({'Status': 'Success', 'coin' : user.coin})

        return ({'Status':'Try Again'})
