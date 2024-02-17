# create_tables.py
from app import create_app
from db import db
from models import User

# Create the Flask application instance
app = create_app()

# Use the application context
with app.app_context():
    # Create the tables
    db.create_all()
