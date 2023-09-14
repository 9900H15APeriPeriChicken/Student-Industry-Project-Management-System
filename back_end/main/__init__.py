import os
from flask import Flask
# from flask_login import LoginManager
from back_end.main.config import config_type
from back_end.main.api import api_bp
from back_end.main.extension import db,cors
from back_end.main.models import User

basedir = os.path.abspath(os.path.dirname(__file__))
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'

def create_app(config_class='default'):
    app = Flask(__name__)
    setup_app(app, config_class)
    setup_blueprints(app)
    setup_extension(app)
    return app

def setup_app(app, config_class):
    app.config.from_object(config_type[config_class])
    config_type[config_class].init_app(app)
    app.url_map.strict_slashes = False

def setup_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')

def setup_extension(app):
    db.init_app(app)
    cors.init_app(app)





