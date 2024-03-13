# app/views/user_views.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User
from app import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template('user_detail.html', user=user)
    else:
        return render_template('error.html', message='User not found'), 404

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.form
    new_user = User(username=data['username'], email=data['email'])
    # Add additional fields as needed
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('user.get_users'))

# Add more routes and views as needed
