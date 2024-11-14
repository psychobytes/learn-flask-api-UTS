from flask import Blueprint
from controllers.DifficultyController import get_difficulties, get_difficulty, add_difficulty, update_difficulty, delete_difficulty

difficulty_bp = Blueprint('Difficulty_bp', __name__)

difficulty_bp.route('/api/difficulty', methods=['GET'])(get_difficulties)
difficulty_bp.route('/api/difficulty/<int:id>', methods=['GET'])(get_difficulty)
difficulty_bp.route('/api/difficulty', methods=['POST'])(add_difficulty)
difficulty_bp.route('/api/difficulty/<int:id>', methods=['PUT'])(update_difficulty)
difficulty_bp.route('/api/difficulty/<int:id>', methods=['DELETE'])(delete_difficulty)
