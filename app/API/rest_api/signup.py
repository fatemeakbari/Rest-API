
from flask_restplus import Resource
from flask import jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
from Models import *
from dashboard import redis_store, api, isValidEmail
from API.dataModel import signup_model
import uuid


ns = api.namespace('/')

@ns.route('/signup')
class SignUp(Resource):

    @api.expect(signup_model)
    def post(self):

        """
        signup user
        """

        # get info from user
        data = request.json
        username = data['username']
        password = data['password']
        email = data['email']
        nickname = data['nickname']


        if not username or not password or not email or not nickname :
            return ({'Status': 'please fill all fields'})

        if not isValidEmail(email):
            return ({'Status' : 'email invalid'})

        exist_user = User.get_user_by_username(username)
        if exist_user:
            return ({'Status': 'username already exist'})

        exist_user = User.get_user_by_email(email)
        if exist_user:
            return ({'Status': 'email already exist'})

        #save user in db
        password_hash = generate_password_hash(password, method='sha256')
        new_user = User(username,password_hash, email, nickname)
        user = new_user.save_to_db()

        #session
        if user:
            username_hash = hashlib.sha256(username.encode()).hexdigest()
            session_id = redis_store.set_item(key = username_hash, value = username)
            return ({ 'Status': 'Success', "session_id": session_id}), 200

        else:
            return ({"Status": "Try again"})
