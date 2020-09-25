
from flask_sqlalchemy import SQLAlchemy
from auth import RedisStore
from flask_restplus import Api
from Models import *
import re


db = SQLAlchemy()

redis_store = RedisStore()
api = Api(version ='1.0', title='Nimble Knight Document', description="simple doc of nimble knight's API")


def isValidEmail(email):
    if len(email) > 7:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email) != None:
            return True
        return False
    return False
