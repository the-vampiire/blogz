from app import DB, SESSION
from validate_email import validate_email # https://pypi.python.org/pypi/validate_email
from passlib.hash import pbkdf2_sha256 # https://passlib.readthedocs.io/en/stable/

class User(DB.Model):
  __tablename__ = "users" # override model name for plurality convention 

  id = DB.Column(DB.Integer, primary_key = True)
  username = DB.Column(DB.String(20), unique = True, nullable = False)
  password = DB.Column(DB.String(30), nullable = False)
  email = DB.Column(DB.String(30), unique = True, nullable = True)

  # User instance: user.blogs = list of user's blogs
  blogs = DB.relationship("Blog", backref = "User", lazy = "joined")

  def verify_email(self, email):
    return validate_email(email)

  def hash_password(self, password):
    if not re.match(re.compile('[0-9]{2,}'), password): 
        return {'password_error': 'Password must contain at least two digits.'}
    elif not re.match(re.compile('[A-Z]{1,}'), password): 
        return {'password_error': 'Password must contain at least one uppercase letter.'}
    elif not re.match(re.compile('\W?'), password): 
        return {'password_error': 'Password must contain at least one special character: [ !, @, #, $, &, * ].'}
    return pbkdf2_sha256(password)