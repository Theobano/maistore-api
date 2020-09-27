import os
from blacklist import BLACKLIST
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Resource, Api, reqparse
from routes import route_path

"""

    Flask is the main framework for the project
    flask_jwt is used for authentication via tokens
    flask_restful makes working with flask alot easier
    Flask SQLAlchemy is used to easily store data to a relational database
"""

#export PATH="$PATH:/home/vcode/.local/bin"
#runner : reset && python app.py

def create_app(secret_key):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ["access", "refresh"]
    app.secret_key = secret_key #always remember to get the apps's secret key, also this key should be hidden from the public.
    
    return app

def create_api(app):
    api = Api(app=app)
    return api
    
def link_jwt(app):
    return JWTManager(app) #creates a new end point called */auth*

def link_route_path(api):
    for route, path in route_path: api.add_resource(route, *path)
    return api

# create app
app = create_app(secret_key="vcode")
api = create_api(app)
jwt = link_jwt(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:  # best to read this from a config file or database
        return {"userid" : 1, "is_admin" : True}
    return {"userid" : identity, "is_admin" : False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST

@jwt.expired_token_loader
def expire_token_callback():
    return jsonify({
    "description" : "The token has expired",
    "error" : "token_expired"
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
    "description" : "Token is not valid",
    "error" : "invalid_expired"
    }), 401

@jwt.unauthorized_loader
def missing_token_callback():
    return jsonify({
    "description" : "Request does not contain an access token.",
    "error" : "authorization_required"
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
    "description" : "token not fresh.",
    "error" : "fresh_token_required"
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
    "description" : "The token has been revoked",
    "error" : "token_revoked"
    }), 401

link_route_path(api=api)

if __name__ == "__main__":
    from db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(port=5000, debug=True)