import unicodedata
from flask import render_template, request, session, redirect, url_for
from flask_login import current_user

from app.extensions import db
from app.models.stats import FlagStat
from app.data.flags_data import FLAG_SETS

# Import the blueprint from the game module
from app.game import game_bp

def normalize_str(text):
    """Remove accents, extra spaces, and convert to lowercase."""
    if not text:
        return ""
    return "".join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower().strip()

def update_flag_stat(flag_name, flag_set, is_hit):
    """Helper function to log hits and misses for logged-in users."""
    if not current_user.is_authenticated:
        return

    stat = FlagStat.query.filter_by(
        user_id=current_user.id,
        flag_name=flag_name,
        flag_set=flag_set
    ).first()

    # If the user hasn't encountered this flag yet, create a new record
    if not stat:
        stat = FlagStat(
            user_id=current_user.id, 
            flag_name=flag_name, 
            flag_set=flag_set,
            hits=0,
            misses=0
        )
        db.session.add(stat)

    if is_hit:
        stat.hits += 1
    else:
        stat.misses += 1

    db.session.commit()

@game_bp.route('/typing', methods=['GET', 'POST'])
def typing_mode():
    # 1. Validate Session State
    if 'indices' not in session: 
        return redirect(url_for('game.index'))
    
    # 2. Check for Game Completion
    if session['current_idx'] >= len(session['indices']):
        return redirect(url_for('game.victory'))

    # 3. Retrieve Current Flag Data
    set_key = session['flag_set']
    current_country_idx = session['indices'][session['current_idx']]
    country_data = FLAG_SETS[set_key]['data'][current_country_idx]
    
    # 4. Handle User Guess (POST)
    if request.method == 'POST':
        user_input = normalize_str(request.form.get('answer', ''))
        
        # Generate list of valid answers (normalized)
        valid_options = [normalize_str(s) for s in country_data['synonyms']]
        valid_options.append(normalize_str(country_data['name']))

        # In typing mode, the JS frontend only sends if it's correct,
        # but we validate here on the backend for absolute security.
        if user_input in valid_options:
            session['score'] = session.get('score', 0) + 1
            update_flag_stat(country_data['name'], set_key, is_hit=True)
            
            session['current_idx'] += 1
            session.modified = True
            return redirect(url_for('game.typing_mode'))
        else:
            # If a user somehow bypasses JS and submits a wrong answer
            session['errors'] = session.get('errors', 0) + 1
            update_flag_stat(country_data['name'], set_key, is_hit=False)
        
    # 5. Calculate total flags for the progress bar
    total_flags = len(FLAG_SETS[set_key]['data'])

    # Note: Ensure typing.html is moved to app/templates/game/typing.html
    return render_template('game/typing.html', 
                           country=country_data, 
                           folder=session['flag_folder'],
                           start_time=session['start_time'],
                           total_flags=total_flags)