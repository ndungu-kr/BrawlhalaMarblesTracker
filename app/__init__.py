from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'marbles.db'

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = getenv('DB_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .routes import main
    from .auth import auth

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models

    with app.app_context():
        db.create_all()
        print('Database Running...')

    return app
