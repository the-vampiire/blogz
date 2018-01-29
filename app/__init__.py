# Dependencies
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from app.private import DB_URI
from sqlalchemy import create_engine, inspect

# Create Server
app = Flask(__name__)

# Configure Server
app.config['DEBUG'] = True
PORT = 3000 # set the port here

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_ECHO'] = False # set True for MySQL report on database activity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)
SESSION = DB.session
ENGINE = create_engine(DB_URI)
INSPECTOR = inspect(ENGINE) # used for checking if tables exist on startup