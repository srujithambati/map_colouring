import bcrypt
from flask import Blueprint, app, redirect,render_template, request

from models import User
from app import db

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('signup.html')
    

@views.route('/signup', methods=['POST'])
def signup():
    # Retrieve form data
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = hash_password(password)

    # Create a new User object
    new_user = User(username=username, email=email, password=hashed_password)
    
    # Add the new user to the database session
    db.session.add(new_user)
    db.session.commit()
    
    # Redirect to a success page or display a success message
    return redirect('/login')

@views.route('/login')
def success():
    return 'You have successfully signed up!'


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

