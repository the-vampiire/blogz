from app import db # import the database instance from app.py
from validate_email import validate_email
from passlib.hash import pbkdf2_sha256

class User(db.Model):
  __tablename__ = "users" # override model name for plurality 

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(50), unique = True, nullable = False)
  password = db.Column(db.String(30), nullable = False)
  blogs = db.relationship("Blog", backref = "User", lazy = "joined")

  def verify_email(email):
    return validate_email(email)

  def hash_password(password):
    return pbkdf2_sha256(password)
    
