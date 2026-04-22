from flask import Blueprint

# 1. Define the Blueprint here, globally for the game module
game_bp = Blueprint('game', __name__)

# 2. Import all your route files AFTER defining the blueprint
# This registers all the routes from all three files to the game_bp object!
from app.game import routes, multiple, typing