from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from flask_babel import _

from app.extensions import db
from app.models.stats import FlagStat
from app.models.game import GameSession
from app.models.user import User

profile_bp = Blueprint('profile', __name__)

def get_user_tier(user_id, mode, flag_set):
    """Calculates the user's quartile tier for a specific mode and set based on flawless runs."""
    valid_runs = db.session.query(
        GameSession.user_id,
        func.min(GameSession.time_taken).label('best_time')
    ).filter(
        GameSession.mode == mode,
        GameSession.flag_set == flag_set,
        GameSession.errors == 0  # Only flawless runs count for the ranking
    ).group_by(GameSession.user_id).subquery()
    
    ranked_query = db.session.query(
        valid_runs.c.user_id,
        func.ntile(4).over(order_by=valid_runs.c.best_time).label('quartile')
    ).subquery()

    user_rank = db.session.query(ranked_query.c.quartile).filter(ranked_query.c.user_id == user_id).first()
    
    if user_rank:
        medals = {1: 'Diamond', 2: 'Gold', 3: 'Silver', 4: 'Bronze'}
        return medals.get(user_rank.quartile, 'Unranked')
    return 'Unranked'

@profile_bp.route('/')
@login_required
def dashboard():
    # 1. Global & Accuracy Stats
    total_games = GameSession.query.filter_by(user_id=current_user.id).count()
    total_hits = db.session.query(func.sum(FlagStat.hits)).filter_by(user_id=current_user.id).scalar() or 0
    total_misses = db.session.query(func.sum(FlagStat.misses)).filter_by(user_id=current_user.id).scalar() or 0
    accuracy = round((total_hits / (total_hits + total_misses) * 100), 1) if (total_hits + total_misses) > 0 else 0

    # 2. Top and Bottom Flags
    most_missed = FlagStat.query.filter_by(user_id=current_user.id).order_by(desc(FlagStat.misses)).limit(5).all()
    most_hit = FlagStat.query.filter_by(user_id=current_user.id).order_by(desc(FlagStat.hits)).limit(5).all()

    # 3. Achievements
    achievements = {
        'played_choice': GameSession.query.filter_by(user_id=current_user.id, mode='multiple').first() is not None,
        'played_typing': GameSession.query.filter_by(user_id=current_user.id, mode='typing').first() is not None
    }

    # 4. Calculate all 6 Ranking Tiers
    modes = ['multiple', 'typing']
    sets = ['national', 'world_cup', 'brazil_states']
    
    user_tiers = {}
    for m in modes:
        user_tiers[m] = {}
        for s in sets:
            user_tiers[m][s] = get_user_tier(current_user.id, m, s)

    # 5. Graph Data
    weekly_stats = db.session.query(
        func.date_trunc('week', GameSession.completed_at).label('week'),
        func.min(GameSession.time_taken).label('best_time')
    ).filter(
        GameSession.user_id == current_user.id, 
        GameSession.mode == 'typing',
        GameSession.flag_set == 'national'
    ).group_by('week').order_by('week').all()

    chart_labels = [stat.week.strftime('%Y-%m-%d') for stat in weekly_stats]
    chart_data = [round(stat.best_time, 2) for stat in weekly_stats]

    return render_template('profile/profile.html', 
        total_games=total_games, accuracy=accuracy,
        missed=most_missed, hit=most_hit,
        achievements=achievements, user_tiers=user_tiers, 
        chart_labels=chart_labels, chart_data=chart_data
    )

@profile_bp.route('/update_nickname', methods=['POST'])
@login_required
def update_nickname():
    new_nickname = request.form.get('nickname').strip()
    if new_nickname:
        try:
            current_user.nickname = new_nickname
            db.session.commit()
            flash(_('Nickname updated successfully!'), 'success')
        except IntegrityError:
            db.session.rollback()
            flash(_('That nickname is already taken.'), 'error')
    return redirect(url_for('profile.dashboard'))