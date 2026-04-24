from flask import render_template
from flask_login import current_user
from sqlalchemy import func

from app.extensions import db
from app.models.game import GameSession
from app.models.user import User
from app.ranking import ranking_bp

@ranking_bp.route('/')
def index():
    modes = ['multiple', 'typing']
    sets = ['national', 'world_cup', 'brazil_states']
    
    leaderboards = {}
    
    for m in modes:
        leaderboards[m] = {}
        for s in sets:
            # 1. Base Subquery: Minimum time for flawless runs per user
            subq = db.session.query(
                GameSession.user_id,
                func.min(GameSession.time_taken).label('best_time')
            ).filter(
                GameSession.mode == m,
                GameSession.flag_set == s,
                GameSession.errors == 0
            ).group_by(GameSession.user_id).subquery()
            
            # 2. Ranked Subquery: Calculate rank over the best times using SQL Window Functions
            ranked_subq = db.session.query(
                subq.c.user_id,
                subq.c.best_time,
                func.rank().over(order_by=subq.c.best_time).label('rank')
            ).subquery()

            # 3. Top 10 Players
            top_players = db.session.query(
                User.nickname,
                User.avatar,
                ranked_subq.c.best_time,
                ranked_subq.c.rank
            ).join(
                ranked_subq, User.id == ranked_subq.c.user_id
            ).order_by(ranked_subq.c.rank).limit(10).all()

            # 4. Find the Current User's Specific Rank (If logged in)
            user_rank_data = None
            if current_user.is_authenticated:
                user_rank_data = db.session.query(
                    ranked_subq.c.rank,
                    ranked_subq.c.best_time
                ).filter(ranked_subq.c.user_id == current_user.id).first()

            # Store both pieces of data in the dictionary
            leaderboards[m][s] = {
                'top_players': top_players,
                'user_rank': user_rank_data
            }
            
    return render_template('ranking/index.html', leaderboards=leaderboards)