from app import db # import the database instance from app.py

class Blog(db.Model):
  __tablename__ = "blogs" # override model name for plurality 

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(140), nullable = False)
  body = db.Column(db.Text, nullable = False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  created_at = db.Column(db.String(25), nullable = False, default = dt.now().strftime('%B %d, %Y'))
    
