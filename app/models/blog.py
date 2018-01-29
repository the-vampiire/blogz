from app import db, db_session
from datetime import datetime as dt
from app.models.user import User

class Blog(db.Model):
  __tablename__ = "blogs" # override model name for plurality 

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(140), nullable = False)
  body = db.Column(db.Text, nullable = False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  created_at = db.Column(db.String(25), nullable = False, default = dt.now().strftime('%B %d, %Y'))

  def get_owners(self):
    owner_ids = db_session.query(self.owner_id.distinct()).all()
    return [User.query.get(user_id) for user_id in owner_ids]