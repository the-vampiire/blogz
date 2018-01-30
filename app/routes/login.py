from flask import Blueprint, render_template, request, redirect, session, flash
from app import db_session
from app.models.user import User
from app.models.blog import Blog
 
login_view = Blueprint('login_view', __name__)

@login_view.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == 'GET':
    if 'logged_in' not in session: return render_template('login.html')
    return redirect('/')
  
  username = request.form['username']
  password = request.form['password']

  user = User.query.filter_by(username=username).first()

  if not user:
    flash('No user found with that username. Signup for a new account')
    return redirect('/signup')

  if not user.verify_password(password):
    return render_template('login.html', auth_error="Invalid credentials")

  # create session
  session['logged_in'] = True
  session['username'] = user.username
  session['user_id'] = user.id
  
  return redirect('/')