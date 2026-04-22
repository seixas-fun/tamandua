import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-fallback-secret-key')
    
    # PostgreSQL Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg://localhost/tamandua')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Google OAuth
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    
    # i18n
    LANGUAGES = ['en', 'pt']
    BABEL_DEFAULT_LOCALE = 'en'