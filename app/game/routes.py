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
    return render_template('game/index.html')

@game_bp.route('/start/<mode>')
def setup(mode):
    set_key = request.args.get('set', 'national')
    
    # multilangue support
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


MIN_SECONDS_PER_FLAG = 0.3

@game_bp.route('/victory')
def victory():
    indices = session.get('indices', [])
    current_idx = session.get('current_idx', 0)

    # Anti-cheat: jogo precisa ter sido completado
    if not indices or current_idx < len(indices):
        return redirect(url_for('game.index'))

    mode = session.get('game_mode', 'typing')
    flag_set = session.get('flag_set', 'national')
    hits = session.get('score', 0)
    errors = session.get('errors', 0)
    start_time = session.get('start_time', time.time())
    total_time = round(time.time() - start_time, 2)
    total_flags = len(indices)

    # Anti-cheat: hits + errors deve ser igual ao total de bandeiras
    if hits + errors != total_flags:
        return redirect(url_for('game.index'))

    # Anti-cheat: tempo mínimo humanamente possível (0.3s por bandeira)
    if total_time < total_flags * MIN_SECONDS_PER_FLAG:
        return redirect(url_for('game.index'))

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

    # Limpa estado do jogo para evitar reenvio do mesmo resultado
    for key in ['indices', 'current_idx', 'score', 'errors', 'start_time', 'game_mode', 'flag_set', 'flag_folder']:
        session.pop(key, None)

    return render_template('game/victory.html', mode=mode, time=total_time, hits=hits, errors=errors)

@game_bp.route('/set_language/<lang>')
def set_language(lang):
    # Ensure they only pass valid languages
    if lang in ['en', 'pt', 'es']:
        session['lang'] = lang
    
    # Redirect back to the page they were on, or to index if unknown
    return redirect(request.referrer or url_for('game.index'))