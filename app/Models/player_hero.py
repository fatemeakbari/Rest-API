from flask_sqlalchemy import SQLAlchemy
from .hero import Hero
import datetime
from dashboard import db

class Player_Hero(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    hero_id = db.Column(db.String(256), nullable = False)
    energy = db.Column(db.Float, nullable = False)
    active = db.Column(db.Boolean, default = False)
    recovery_rate = db.Column(db.DateTime,  default=datetime.datetime.now() + datetime.timedelta(minutes=30))
    user_id = db.Column(db.String(), db.ForeignKey('user.username'), nullable=False)

    def __init__(self, hero_id, energy, recovery_rate, user_id):


        self.hero_id = hero_id
        self.energy = energy
        self.user_id = user_id
        self.recovery_rate = recovery_rate


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
        return self


    def delele_from_db(self):
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
    def get_playerHero(self, username):
        try:
            player_hero = Player_Hero.query.filter_by(user_id = username)
            hero_list = []
            for hero in player_hero:
                hero_list.append(int(hero.hero_id))
            return hero_list
        except:
            return None


    @classmethod
    def get_active_playerHero(self, username):
        try:
            player_hero = Player_Hero.query.filter_by(user_id = username)
            hero_list = []
            for hero in player_hero:
                if hero.active:
                    hero_list.append(int(hero.hero_id))
            return hero_list
        except:
            return None


    def get_oneHero(username, hero_id):
        return Player_Hero.query.filter(Player_Hero.user_id == username, Player_Hero.hero_id == hero_id).first()


    @classmethod
    def get_exist_playerHero(self, username, hero_id):
        try:
            player_hero = self.get_oneHero(username, hero_id)
            return player_hero
        except:
            return None


    @classmethod
    def boost_energy(self, username, hero_id):
        try:
            player_hero = self.get_oneHero(username, hero_id)
            hero = Hero.get_hero_by_heroID(hero_id)
            player_hero.energy = hero.energy
            return player_hero
        except:
            return None


    @classmethod
    def start_game(self, username, hero1, hero2, hero3):
        player_hero = Player_Hero.query.filter_by(user_id = username)
        hero_list = []
        for hero in player_hero:
            if(hero.hero_id == hero1 or hero.hero_id == hero2 or hero.hero_id == hero3 ):
                if(hero.energy > 0):
                    hero.energy -= 1
                    hero_list.append(hero.hero_id)
                    hero.active =True
        if self.update_db(self):
            return hero_list
        return None


    #balad nistam khob :)
    def update_energy_by_username(self, username):

        player_hero = Player_Hero.query.filter_by(user_id = username).first()

        for hero in player_hero:
            if( datetime.datetime.now() > hero.recovery_rate()):
                hero.energy += 1
                hero.recovery_rate = datetime.datetime.now() + datetime.timedelta(minutes=30)

                db.session.commit()
