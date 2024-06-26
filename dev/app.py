from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, abort
from extensions import db

from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash
from sqlalchemy import desc

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Flask-Bcrypt
bcrypt = Bcrypt(app)



# Import User model after db creation

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    from models import User
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash_message="Error"
            print("error")
            return render_template('signup.html',flash_message=flash_message)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(fullname=fullname, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    # Pass flashed message to the template
    flash_message = "error"
    print(flash_message)  # Print flashed message for debugging
    return render_template('signup.html', flash_message=flash_message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    from models import User

    error = None  # Initialize error variable
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['fullname'] = user.fullname  # Pass the full name to the session
            return redirect(url_for('welcome'))
        else:
            error = 'Invalid email or password'  # Set the error message
    return render_template('login.html', error=error)  # Pass error message to template


@app.route('/welcome')
def welcome():
    if 'user_id' in session:
        fullname = session['fullname']  # Retrieve full name from session
        id = session['user_id']
        return render_template('welcome.html', fullname=fullname,user_id=id)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove 'user_id' from session
    session.pop('fullname', None)  # Remove 'fullname' from session
    return redirect(url_for('login'))



@app.route('/submit_score', methods=['POST'])
def submit_score():
    from models import Scores  # Import the Scores model

    # Ensure user is logged in
    if 'user_id' not in session:
        abort(401)  # Unauthorized

    # Retrieve user ID from session
    user_id = session['user_id']

    # Retrieve score data from request
    score_data = request.json
    score_value = score_data.get('score')

    # Save score to the database
    if score_value is not None:
        score = Scores(user_id=user_id, score=score_value)
        db.session.add(score)
        db.session.commit()

        # Fetch the 5 most recent scores of the user
        recent_scores = Scores.query.filter_by(user_id=user_id).order_by(desc(Scores.timestamp)).limit(5).all()

        # Convert recent scores to a list of dictionaries for JSON response
        recent_scores_data = [{'score': s.score, 'timestamp': s.timestamp} for s in recent_scores]

        return jsonify({'message': 'Score submitted successfully', 'recent_scores': recent_scores_data}), 200
    else:
        return jsonify({'error': 'Score data missing or incorrect format'}), 400




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


