# Dependencies
from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import DB_URI, SESSION_SECRET

# Create Server
app = Flask(__name__)

# Encryption
bcrypt = Bcrypt(app)

# Configure Server
app.config['DEBUG'] = True
app.secret_key = SESSION_SECRET
PORT = 3000 # set the port here

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_ECHO'] = False # set True for MySQL report on database activity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# App exports
db = SQLAlchemy(app)
db_session = db.session


# Import Routes - THANK FUCK [https://stackoverflow.com/questions/41828711/flask-blueprint-sqlalchemy-cannot-import-name-db-into-moles-file]
from app.routes.index import index
from app.routes.new_user import new_user
from app.routes.new_blog import new_blog
app.register_blueprint(index)
app.register_blueprint(new_user)
app.register_blueprint(new_blog)