from flask import Blueprint, render_template
from app.models.blog import Blog
from app.models.user import User

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def index_page():
  blogs = Blog.query.all()
  users = Blog.get_owners(Blog)
  return render_template('index.html', users=users, blogs=blogs)