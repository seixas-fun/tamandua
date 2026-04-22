from app.extensions import db
from datetime import datetime

class GameSession(db.Model):
    __tablename__ = 'game_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mode = db.Column(db.String(20), nullable=False) # 'typing' or 'multiple'
    flag_set = db.Column(db.String(50), nullable=False)
    time_taken = db.Column(db.Float, nullable=False)
    hits = db.Column(db.Integer, default=0)
    errors = db.Column(db.Integer, default=0)
    completed_at = db.Column(db.DateTime, default=lambda: datetime.now(datetime.timezone.utc))