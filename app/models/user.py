import re
from app import db, bcrypt
from validate_email import validate_email # https://pypi.python.org/pypi/validate_email
from passlib.hash import pbkdf2_sha256 # https://passlib.readthedocs.io/en/stable/

class User(db.Model):
  __tablename__ = "users" # override model name for plurality convention 

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique = True, nullable = False)
  password = db.Column(db.String(87), nullable = False)
  email = db.Column(db.String(30), unique = True, nullable = True)

  # User instance: user.blogs = list of user's blogs
  blogs = db.relationship("Blog", backref = "User", lazy = "joined")

  def verify_email(self, email):
    return validate_email(email)

  def password_error(self, password):
    if not re.compile('[0-9]{2,}').findall(password): 
        return 'Password must contain at least two digits.'
    elif not re.compile('[A-Z]{1,}').findall(password): 
        return 'Password must contain at least one uppercase letter.'
    elif not re.compile('\W?').findall(password): 
        return 'Password must contain at least one special character: [ !, @, #, $, &, * ].'
    return None

  def hash_password(self, password):
      return bcrypt.generate_password_hash(password).decode('utf-8')

  def check_password (self, password):
      return bcrypt.check_password_hash(self.password, password)
