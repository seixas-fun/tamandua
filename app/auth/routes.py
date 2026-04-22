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
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

@auth_bp.route('/login')
def login():
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth_bp.route('/authorize')
def authorize():
    # Authlib automatically verifies the token using the keys from the metadata URL
    token = google.authorize_access_token()
    
    # Extract the user info directly from the parsed token
    user_info = token.get('userinfo')
    
    if not user_info:
        return "Failed to fetch user info", 400

    user = User.query.filter_by(google_id=user_info['sub']).first()
    
    if not user:
        # Create a default nickname from email
        base_nick = user_info['email'].split('@')[0]
        user = User(
            google_id=user_info['sub'], # 'sub' is the standard OpenID ID field
            email=user_info['email'],
            name=user_info.get('name', 'Player'),
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