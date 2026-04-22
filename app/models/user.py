from app.extensions import db
from flask_login import UserMixin
from datetime import datetime, timezone

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    avatar = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    sessions = db.relationship('GameSession', backref='player', lazy=True)
    flag_stats = db.relationship('FlagStat', backref='player', lazy=True)
