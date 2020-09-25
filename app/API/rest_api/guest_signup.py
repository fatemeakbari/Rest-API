from flask import make_response
from flask_restplus import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from Models import *
from dashboard import redis_store, api
from uuid import uuid4
import hashlib
import string
import random


ns = api.namespace('/')

@ns.route('/signupAsGuest')
class SignupAsGuest(Resource):


    def post(self):
        """
         create guest user
        """
        chars = string.ascii_uppercase + string.digits
        #create randon username and pass

        username = ''.join(random.choice(chars) for _ in range(8))
        password = ''.join(random.choice(chars) for _ in range(8))

        while(User.get_user_by_username(username)):
            username = ''.join(random.choice(chars) for _ in range(8))

        #save user in db
        password_hash = generate_password_hash(password, method='sha256')
        new_user = User(username,password_hash, email=None, nickname=None)
        user = new_user.save_to_db()

        #session
        if user:
            username_hash = hashlib.sha256(username.encode()).hexdigest()
            session_id = redis_store.set_item(key = username_hash, value = username)
            return ({'Status': 'Success', 'username': username, 'password' : password, 'session_id': session_id}), 200

        else:
            return ({"Status": "Not Found"})
