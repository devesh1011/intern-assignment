from flask import Flask
from flask_pymongo import PyMongo
from config import Config


def build_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    global mongo
    mongo = PyMongo(app)

    from app.api.user_routes import user_blueprint

    app.register_blueprint(user_blueprint)

    return app
