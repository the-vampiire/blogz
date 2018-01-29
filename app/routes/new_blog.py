from flask import Blueprint, render_template, session, redirect, request
from app import db_session
from app.models.blog import Blog

new_blog = Blueprint('new_blog', __name__)

@new_blog.route('/new_blog', methods=['GET', 'POST'])
def create_blog():
  if request.method == 'GET':
    return render_template('new_blog.html')

  title = request.form['title']
  body = request.form['body']
  owner_id = session['user_id']

  blog = Blog(title=title, body=body, owner_id=owner_id)
  db_session.add(blog)
  db_session.commit()

  blogs = Blog.query.all()
  users = Blog.get_owners(Blog)
  return render_template('index.html', users=users, blogs=blogs)