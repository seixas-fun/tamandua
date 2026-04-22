from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from sqlalchemy import desc
from app.extensions import db
from app.models.stats import FlagStat

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/')
@login_required
def dashboard():
    # Get top 5 most missed flags
    most_missed = FlagStat.query.filter_by(user_id=current_user.id)\
                                .order_by(desc(FlagStat.misses))\
                                .limit(5).all()
                                
    # Get recent games
    from app.models.game import GameSession
    recent_games = GameSession.query.filter_by(user_id=current_user.id)\
                                    .order_by(desc(GameSession.completed_at))\
                                    .limit(10).all()

    return render_template('profile.html', missed=most_missed, history=recent_games)