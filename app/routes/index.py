from flask import Blueprint, render_template, session
from sqlalchemy import desc
from app.models.blog import Blog
from app.models.user import User

index_view = Blueprint('index_view', __name__)

@index_view.route('/', methods=['GET'])
def index():
  blogs = Blog.query.order_by(desc(Blog.id)).all() # order by most recent entry
  print(type(blogs))
  users = Blog.get_owners(Blog)
  print(type(users))
  return render_template('index.html', users=users, blogs=blogs, session=session)