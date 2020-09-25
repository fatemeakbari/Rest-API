from flask_restplus import Resource
from flask import request, make_response

from werkzeug.security import check_password_hash
import hashlib

from dashboard import redis_store
from Models import *
from dashboard import api
from API.dataModel import login_model
ns = api.namespace('/')


@ns.route('/login')
class Login(Resource):

    @api.expect(login_model)
    def post(self):
        """
        login
        """
        data = request.json
        username = data['username']
        password = data['password']


        if not data or not username or not password:
            return ({'Status': 'Please Fill All Fields'})

        user = User.get_user_by_username(username)

        if  user == None:
            return ({'Status': 'Please Signup'})

        if check_password_hash(user.password, password):

            username_hash = hashlib.sha256(username.encode()).hexdigest()
            session_id = redis_store.set_item(key = username_hash, value = username)

            return ({'Status': 'Success', 'session_id': session_id}), 200

        return ({'Status': 'The Password Is Incorrect'})
