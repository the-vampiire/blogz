# Dependencies
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from private import DB_URI
from datetime import datetime

# Create Server
app = Flask(__name__)

# Configure Server
app.config['DEBUG'] = True

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI # imported from private.py
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)