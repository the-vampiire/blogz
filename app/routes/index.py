from flask import Blueprint, render_template, session
from sqlalchemy import desc
from app.models.blog import Blog
from app.models.user import User

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def index_page(): 
  if 'logged_in' in session:
    user = {
      "id": session['user_id'],
      "username": session['username']
    }
  else:
    user = None

  blogs = Blog.query.order_by(desc(Blog.id)) # order by most recent entry
  users = Blog.get_owners(Blog)
  return render_template('index.html', users=users, blogs=blogs, user=user)