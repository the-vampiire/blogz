from app import DB, SESSION
from models.user import User
from datetime import datetime as dt

class Blog(DB.Model):
  __tablename__ = "blogs" # override model name for plurality 

  id = DB.Column(DB.Integer, primary_key = True)
  title = DB.Column(DB.String(140), nullable = False)
  body = DB.Column(DB.Text, nullable = False)
  owner_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'), nullable = False)
  created_at = DB.Column(DB.String(25), nullable = False, default = dt.now().strftime('%B %d, %Y'))

  def get_owners(self):
    owner_ids = SESSION.query(self.owner_id.distinct()).all()
    return [User.query.get(user_id) for user_id in owner_ids]