from sqlalchemy import func
from app.models.game import GameSession

def get_ranking(mode, category):
    return (
        db.session.query(
            GameSession.user_id,
            func.max(GameSession.score).label("best_score")
        )
        .filter_by(mode=mode, category=category)
        .group_by(GameSession.user_id)
        .order_by(func.max(GameSession.score).desc())
        .limit(100)
        .all()
    )