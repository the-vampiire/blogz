from flask import Blueprint, session, redirect, request, flash
from app import db_session
from app.models.blog import Blog

new_blog = Blueprint('new_blog', __name__)

@new_blog.route('/new_blog', methods=['POST'])
def create_blog():
  if 'logged_in' not in session:
    flash("Not logged in", category='errors')
    return redirect('/')
  else:
    title = request.form['title']
    body = request.form['body']
    owner_id = session['user_id']

    blog = Blog(title=title, body=body, owner_id=owner_id)
    db_session.add(blog)
    db_session.commit()

  return redirect('/blog/{}'.format(blog.id))