from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marbles.db'
    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()
        print("Database running...")

    from .routes import main
    app.register_blueprint(main)

    return app