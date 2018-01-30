from flask import Blueprint, render_template, session
from app.models.user import User

user_view = Blueprint('user_view', __name__)

@user_view.route('/user/<int:id>')
def blog_user(id):
  return render_template("user.html", user=User.query.get(id), session=session)
