from dashboard import db
import datetime

class Hero(db.Model):
    hero_id = db.Column(db.Integer, primary_key = True)
    max_health = db.Column(db.Float)
    damage_per_hit = db.Column(db.Float)
    defence = db.Column(db.Float)
    energy = db.Column(db.Float)
    stamina = db.Column(db.Float, default =100)
    price = db.Column(db.Integer)
    minimumRequiredLevel = db.Column(db.Integer, default = 1)
    recovery_rate = db.Column(db.DateTime,  default=datetime.datetime.now() + datetime.timedelta(minutes=30))
    #max_energy = db.Column(db.Integer)

    mass = db.Column(db.Float, default = 100)
    drag = db.Column(db.Float, default = 100)
    angularVelocity = db.Column(db.Float, default = 100)
    init_velocity = db.Column(db.Float, default = 100)



    def __init__(self,hero_id, max_health, damage_per_hit, defence, energy, stamina, price, minimumRequiredLevel, recovery_rate):

        self.hero_id = hero_id
        self.max_health = max_health
        self.damage_per_hit = damage_per_hit
        self.defence = defence
        self.energy = energy
        self.stamina = stamina
        self.price = price
        self.minimumRequiredLevel = minimumRequiredLevel
        self.recovery_rate = recovery_rate




    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
        return self



    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self
        except:
            return None
            
    @classmethod
    def get_hero_by_heroID(self,hero_id):
        try:

            hero = Hero.query.filter_by(hero_id = hero_id).first()
            return hero
        except:
            return None
