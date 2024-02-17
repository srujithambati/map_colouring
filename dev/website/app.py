from flask import Flask
from views import views
from db import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hsahdasd hahdashda'
    app.register_blueprint(views, url_prefix='/')

    # Use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a@localhost/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return app
