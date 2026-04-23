import time
import random
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import current_user

from app.extensions import db
from app.models.game import GameSession
from app.models.stats import FlagStat
from app.profile.routes import get_user_tier
from app.data.flags_data import FLAG_SETS
from app.game import game_bp

@game_bp.route('/')
def index():
    tier = 'Unranked'
    best_time = None
    if current_user.is_authenticated:
        tier = get_user_tier(current_user.id)
        
        # Fetch the user's absolute best flawless run in typing mode
        best_run = GameSession.query.filter_by(
            user_id=current_user.id, 
            mode='typing', 
            errors=0
        ).order_by(GameSession.time_taken.asc()).first()
        
        if best_run:
            best_time = best_run.time_taken

        # Pass the variables to the template
    return render_template('game/index.html', tier=tier, best_time=best_time)

@game_bp.route('/start/<mode>')
def setup(mode):
    set_key = request.args.get('set', 'national')
    if set_key not in FLAG_SETS:
        set_key = 'national'
    
    session['flag_folder'] = FLAG_SETS[set_key]['folder']
    chosen_set = FLAG_SETS[set_key]['data']

    indices = list(range(len(chosen_set)))
    random.shuffle(indices)
    
    session['game_mode'] = mode
    session['flag_set'] = set_key
    session['indices'] = indices
    session['current_idx'] = 0
    session['score'] = 0
    session['errors'] = 0
    session['start_time'] = time.time()
    
    return redirect(url_for(f'game.{mode}_mode'))


@game_bp.route('/victory')
def victory():
    mode = session.get('game_mode', 'typing')
    flag_set = session.get('flag_set', 'national')
    hits = session.get('score', 0)
    errors = session.get('errors', 0)
    start_time = session.get('start_time', time.time())
    total_time = round(time.time() - start_time, 2)
    
    # If user is logged in, save to database
    if current_user.is_authenticated:
        game_record = GameSession(
            user_id=current_user.id,
            mode=mode,
            flag_set=flag_set,
            time_taken=total_time,
            hits=hits,
            errors=errors
        )
        db.session.add(game_record)
        db.session.commit()
        # Note: FlagStat updates for misses would happen during the gameplay routes 
        # (e.g., in multiple_mode POST request).

    return render_template('game/victory.html', mode=mode, time=total_time, hits=hits, errors=errors)

@game_bp.route('/set_language/<lang>')
def set_language(lang):
    # Ensure they only pass valid languages
    if lang in ['en', 'pt']:
        session['lang'] = lang
    
    # Redirect back to the page they were on, or to index if unknown
    return redirect(request.referrer or url_for('game.index'))