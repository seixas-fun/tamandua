from flask import Blueprint, redirect, url_for, session
from flask_login import login_user, logout_user, login_required
from app.extensions import oauth, db
from app.models.user import User
import os

auth_bp = Blueprint('auth', __name__)

google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)

@auth_bp.route('/login')
def login():
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth_bp.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    
    user = User.query.filter_by(google_id=user_info['id']).first()
    if not user:
        # Create a default nickname from email
        base_nick = user_info['email'].split('@')[0]
        user = User(
            google_id=user_info['id'],
            email=user_info['email'],
            name=user_info['name'],
            nickname=base_nick,
            avatar=user_info.get('picture')
        )
        db.session.add(user)
        db.session.commit()
        
    login_user(user)
    return redirect(url_for('game.index'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('game.index'))