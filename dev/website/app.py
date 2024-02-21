# from flask import Flask
# from views import views
# from flask_sqlalchemy import SQLAlchemy
# import os
# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'hsahdasd hahdashda'
#     app.register_blueprint(views, url_prefix='/')

#     # Use PostgreSQL database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a@localhost/postgres'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db = SQLAlchemy()
#     db.init_app(app)
#     return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:a@localhost/postgres')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



if __name__ == '__main__':
    app.run()