from flask import Blueprint, render_template, session
from app.models.blog import Blog

blog_view = Blueprint('blog_view', __name__)

@blog_view.route('/blog/<int:id>', methods = ['GET'])
def blog(id):
  blog = Blog.query.get(id)
  owner = blog.get_owner()
  return render_template("blog.html", blog=blog, owner=owner, session=session)