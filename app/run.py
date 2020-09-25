from flask import Flask, redirect, render_template, url_for, request, Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from API import *
from Models import *
from init_db import init_hero
from dashboard import db, api

flask_app = Flask(__name__)
admin = Admin()




#database config
flask_app.config['POSTGRES_USER'] = 'fateme'
flask_app.config['POSTGRES_PW'] = '123456'
flask_app.config['POSTGRES_DB'] = 'nimble_knight'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fateme:123456@postgres:5432/nimble_knight'

#app config
flask_app.config['DEBUG'] = True


#swagger config
flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
flask_app.config['RESTPLUS_VALIDATE'] = True
flask_app.config['RESTPLUS_MASK_SWAGGER'] = False



blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
#api.add_namespace(blog_posts_namespace)
flask_app.register_blueprint(blueprint)
#---add blueprint ---> bashe khob hala :)

import time
time.sleep(5)

db.app = flask_app
db.init_app(flask_app)
db.create_all()

init_hero()


admin = Admin(flask_app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Player_Hero, db.session))
admin.add_view(ModelView(Hero, db.session))


if __name__ == '__main__':
     flask_app.run(host='0.0.0.0', port=5008)
