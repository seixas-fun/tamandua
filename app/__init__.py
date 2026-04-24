from flask import Flask, request, session
from app.config import Config
from app.extensions import db, migrate, login_manager, babel, csrf, oauth
from app.auth.routes import auth_bp
from app.game import game_bp
from app.profile.routes import profile_bp
from app.ranking import ranking_bp


def get_locale():
    # Check if user selected a language, otherwise use browser default
    return session.get('lang', request.accept_languages.best_match(Config.LANGUAGES))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    babel.init_app(app, locale_selector=get_locale)
    csrf.init_app(app)
    oauth.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(game_bp)
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(ranking_bp, url_prefix='/ranking')

    return app