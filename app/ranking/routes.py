from flask import Blueprint, render_template, redirect, url_for
from sqlalchemy import func, desc
from app.extensions import db
from app.models.game import GameSession
from app.models.user import User

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/')
def index():
    # Set the default leaderboard to "national" flags in "typing" mode
    return redirect(url_for('ranking.typing_ranking', flag_set='national'))

@ranking_bp.route('/typing/<flag_set>')
def typing_ranking(flag_set):
    # 15 minutes = 900 seconds
    TIME_LIMIT = 900 
    
    # Subquery: Users who completed within 15 mins with 0 errors
    valid_runs = db.session.query(
        GameSession.user_id,
        func.min(GameSession.time_taken).label('best_time')
    ).filter(
        GameSession.mode == 'typing',
        GameSession.flag_set == flag_set,
        GameSession.time_taken <= TIME_LIMIT,
        GameSession.errors == 0
    ).group_by(GameSession.user_id).subquery()
    
    # Main query with Quartiles
    ranked_query = db.session.query(
        User.nickname,
        User.avatar,
        valid_runs.c.best_time,
        func.ntile(4).over(order_by=valid_runs.c.best_time).label('quartile')
    ).join(User, User.id == valid_runs.c.user_id).order_by(valid_runs.c.best_time).limit(100).all()

    # Map quartiles to medals
    medals = {1: 'Diamond', 2: 'Gold', 3: 'Silver', 4: 'Bronze'}
    results = [
        {
            "rank": idx + 1,
            "nickname": r.nickname,
            "time": r.best_time,
            "tier": medals.get(r.quartile)
        } for idx, r in enumerate(ranked_query)
    ]
    
    return render_template('ranking.html', leaderboards=results, mode='Typing', flag_set=flag_set)