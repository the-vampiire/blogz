from flask import Blueprint, render_template
from app.models.blog import Blog

blog = Blueprint('blog', __name__)

@blog.route('/blog/<int:id>', methods = ['GET'])
def blog_page(id):
  blog = Blog.query.get(id)
  owner = blog.get_owner()
  return render_template("blog.html", blog=blog, owner=owner)