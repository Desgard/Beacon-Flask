from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/app_data.db'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)

def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app