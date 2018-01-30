from flask import Blueprint, render_template, request, redirect, session, flash
from app import db_session
from app.models.user import User
from app.models.blog import Blog

signup_view = Blueprint('signup_view', __name__) 

@signup_view.route('/signup', methods = ['GET', 'POST'])
def signup():
  if session and session['logged_in']:
    return redirect('/')

  if request.method == 'GET':
    return render_template("signup.html")

  username = request.form['username']
  raw_password = request.form['password']
  verify_password = request.form['verify_password']
  email = request.form['email'] or None

# Route-level validation
  password_error = User.password_error(User, raw_password) or None
  verify_password_error = 'Passwords do not match' if raw_password != verify_password else None 
  email_error = 'Invalid email address' if email and not User.verify_email(User, email) else None

# Error response
  if verify_password_error: flash(verify_password_error, category='errors')
  if password_error: flash(password_error, category='errors')
  if email_error: flash(email_error, category='errors')

  if verify_password_error or password_error or email_error:
    return render_template('signup.html', username=username, email=email)

# All clear - create user
 
  #create and store user
  user = User(username=username, raw_password=raw_password, email=email)
  db_session.add(user)
  db_session.commit()

  # create session
  session['logged_in'] = True
  session['username'] = user.username
  session['user_id'] = user.id
  
  return redirect('/user/{}'.format(user.id))
  

  
