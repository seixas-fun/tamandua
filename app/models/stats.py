from app.extensions import db

class FlagStat(db.Model):
    __tablename__ = 'flag_stats'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    flag_name = db.Column(db.String(100), nullable=False)
    flag_set = db.Column(db.String(50), nullable=False)
    hits = db.Column(db.Integer, default=0)
    misses = db.Column(db.Integer, default=0)