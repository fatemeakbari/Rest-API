from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from .player_hero import Player_Hero
from sqlalchemy.orm import relationship
from dashboard import db




class User( db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(128), unique = True, nullable = False)
    email = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(128), nullable = False)
    nickname = db.Column(db.String(128))
    coin = db.Column(db.Integer, default = 1000)
    level = db.Column(db.Integer, default = 1)
    hero = db.relationship('Player_Hero', backref='user', lazy=True)




    def __init__(self, username, password, email, nickname):
        self.username = username
        self.password = password
        self.email = email
        self.nickname = nickname


    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return None

    def delete_form_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self
        except:
            return None

    def update_db(self):
        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def get_user_by_username(self,username):
        try:
            user = User.query.filter_by(username = username).first()
            return user
        except:
            return None

    @classmethod
    def get_user_by_email(self, email):
        try:
            user = User.query.filter_by(email = email).first()
            return user
        except:
            return None
    '''
    def update_username(self, old_username, new_username):
        try:
            user = User.query.filter_by(username = old_username).first()
            user.name = new_username
            db.session.commit()
            return user
        except:
            return None
    '''
    def buy_coin():
        pass

    @classmethod
    def check_coin(self, user_coin, hero_price):

        if user_coin >= hero_price :
            return True
        return False

    @classmethod
    def check_level(self, user_level, hero_level):

        if user_level >= hero_level :
            return True
        return False

    @classmethod
    def get_coin(self, username):
        try:
            user = User.query.filter_by(username = username).first()
            return user.coin
        except:
            return None

    def update_coin(self, change):
        self.coin += change

    @classmethod
    def get_nickname_by_username(self, username):
        try:
            user = User.query.filter_by(username = username).first()
            return user.nickname
        except:
            return None
    def set_level(self, username, new_level):

         try:
             user = User.query.filter_by(username = username).first()
             user.level = new_level
             db.session.commit()
             return user
         except:
            return None
