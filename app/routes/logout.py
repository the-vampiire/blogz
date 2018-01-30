from flask import Blueprint, redirect, session

logout = Blueprint('logout', __name__)

@logout.route('/logout', methods = ['GET'])
def logout_action():
  session.clear()
  return redirect('/')