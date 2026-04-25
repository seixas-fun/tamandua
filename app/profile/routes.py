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

def get_tier_label(tier):
    """Translates a stable tier key for display without changing internal values."""
    labels = {
        "Diamond": _("Diamond"),
        "Gold": _("Gold"),
        "Silver": _("Silver"),
        "Bronze": _("Bronze"),
        "Unranked": _("Unranked"),
    }
    return labels.get(tier, _("Unranked"))

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

    # 3. Calculate all 6 Ranking Tiers
    modes = ['multiple', 'typing']
    sets = ['national', 'world_cup', 'brazil_states']
    
    user_tiers = {}
    for m in modes:
        user_tiers[m] = {}
        for s in sets:
            user_tiers[m][s] = get_user_tier(current_user.id, m, s)

    # 4. Achievements (Moved below rankings so we can check for Diamond)
    has_diamond = any(tier == 'Diamond' for mode in user_tiers.values() for tier in mode.values())

    achievements = {
        'played_choice': GameSession.query.filter_by(user_id=current_user.id, mode='multiple').first() is not None,
        'played_typing': GameSession.query.filter_by(user_id=current_user.id, mode='typing').first() is not None,
        'played_national': GameSession.query.filter_by(user_id=current_user.id, flag_set='national').first() is not None,
        'played_world_cup': GameSession.query.filter_by(user_id=current_user.id, flag_set='world_cup').first() is not None,
        'played_brazil': GameSession.query.filter_by(user_id=current_user.id, flag_set='brazil_states').first() is not None,
        'flawless_choice': GameSession.query.filter_by(user_id=current_user.id, mode='multiple', errors=0).first() is not None,
        # Check for 0 hits and more than 0 errors (ensures they actually played and didn't just quit instantly)
        'all_wrong_choice': GameSession.query.filter(GameSession.user_id == current_user.id, GameSession.mode == 'multiple', GameSession.hits == 0, GameSession.errors > 0).first() is not None,
        # Time taken is strictly under 10 mins (600s) and 0 errors
        'speedrun_national': GameSession.query.filter(GameSession.user_id == current_user.id, GameSession.mode == 'typing', GameSession.flag_set == 'national', GameSession.errors == 0, GameSession.time_taken <= 600).first() is not None,
        # Time taken is strictly under 2 mins (120s) and 0 errors
        'speedrun_states': GameSession.query.filter(GameSession.user_id == current_user.id, GameSession.mode == 'typing', GameSession.flag_set == 'brazil_states', GameSession.errors == 0, GameSession.time_taken <= 120).first() is not None,
        'diamond_rank': has_diamond
    }

    # 5. Graph Data (Evolution by Attempt for all modes/sets)
    all_sessions = GameSession.query.filter_by(user_id=current_user.id).order_by(GameSession.id.asc()).all()

    evolution_data = {
        'multiple': {'national': [], 'world_cup': [], 'brazil_states': []},
        'typing': {'national': [], 'world_cup': [], 'brazil_states': []}
    }

    for session in all_sessions:
        m = session.mode
        s = session.flag_set
        if m in evolution_data and s in evolution_data[m]:
            evolution_data[m][s].append(round(session.time_taken, 2))

    return render_template('profile/profile.html', 
        total_games=total_games, accuracy=accuracy,
        missed=most_missed, hit=most_hit,
        achievements=achievements, user_tiers=user_tiers, 
        evolution_data=evolution_data, tier_label=get_tier_label
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
