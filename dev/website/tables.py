# create_tables.py
from app import app,db
from models import User

# Create the Flask application instance

# Use the application context
with app.app_context():
    # Create the tables
    db.create_all()
