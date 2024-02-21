from flask import Flask
from flask_migrate import Migrate
from app import db
app = Flask(__name__)
# Adjust the database URI for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a@localhost/postgres'
migrate = Migrate(app, db)


