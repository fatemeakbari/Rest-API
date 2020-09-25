from flask_restplus import fields
from dashboard import api

signup_model = api.model('signup_model', {
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'nickname': fields.String(),

})


login_model = api.model('login_model', {
    'username': fields.String(required=True),
    'password': fields.String(required=True),

})

buy_hero_model = api.model('buyHero_model', {
    'session_id':fields.String(required = True),
    'hero_id':fields.Integer(required = True),
})

boost_hero_model = api.model('boostHero_model', {
    'session_id':fields.String(required = True),
    'hero_id':fields.Integer(required = True),
})

startGame_model = api.model('startGame_model', {
    'username1':fields.String(required = True),
    'username2':fields.String(required = True),
})

startGame_model2 = api.model('startGame_model2', {
    'hero1':fields.Integer(required = True),
    'hero2':fields.Integer(required = True),
    'hero3':fields.Integer(required = True),
    'session_id':fields.String(required = True),
})


buyCoin_model = api.model('buyCoin_model', {
    'session_id':fields.String(required = True),
    'numCoin':fields.Integer(required = True),
})


session_id = api.model('session_id', {
    'session_id':fields.String(required = True),

})
