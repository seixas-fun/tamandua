from flask import render_template, request, session, redirect, url_for
from flask_login import current_user
import random
from app.extensions import db
from app.models.stats import FlagStat
from app.data.flags_data import FLAG_SETS, get_display_name
from app.game import game_bp 

def update_flag_stat(flag_name, flag_set, is_hit):
    """Helper function to log hits and misses for logged-in users."""
    if not current_user.is_authenticated:
        return

    stat = FlagStat.query.filter_by(
        user_id=current_user.id,
        flag_name=flag_name,
        flag_set=flag_set
    ).first()

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


@game_bp.route('/multiple', methods=['GET', 'POST'])
def multiple_mode():
    # 1. Validate Session State
    if 'indices' not in session: 
        return redirect(url_for('game.index'))

    # 2. Check for Game Completion
    if session['current_idx'] >= len(session['indices']):
        return redirect(url_for('game.victory'))

    # 3. Retrieve Current Flag Data
    set_key = session['flag_set']
    lang = session.get('lang', 'en')
    current_country_idx = session['indices'][session['current_idx']]
    correct_country = FLAG_SETS[set_key]['data'][current_country_idx]
    
    # 4. Handle User Guess (POST)
    if request.method == 'POST':
        selected = request.form.get('choice')
        is_correct = (selected == correct_country['name'])
        
        if is_correct:
            session['score'] += 1
        else:
            session['errors'] += 1
            
        # Update PostgreSQL stats for the profile dashboard
        update_flag_stat(correct_country['name'], set_key, is_hit=is_correct)
        
        session['current_idx'] += 1
        session.modified = True
        return redirect(url_for('game.multiple_mode'))

    # 5. Prepare Multiple Choice Options (GET)
    all_flags = FLAG_SETS[set_key]['data']
    others = [c for c in all_flags if c['name'] != correct_country['name']]
    
    # Select 3 random incorrect options and add the correct one
    num_options = min(len(others), 3)
    options = random.sample(others, num_options)
    options.append(correct_country)
    random.shuffle(options)

    option_cards = [
        {
            'value': option['name'],
            'label': get_display_name(option, lang),
            'is_correct': option['name'] == correct_country['name'],
        }
        for option in options
    ]

    total_flags = len(all_flags)
    
    return render_template('game/multiple.html', 
                           country=correct_country, 
                           options=option_cards,
                           folder=session['flag_folder'],
                           total_flags=total_flags)
