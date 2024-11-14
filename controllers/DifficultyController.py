from flask import jsonify, request
from models.DifficultyModel import Difficulty
from config import db

def get_difficulties():
    difficulties = Difficulty.query.all()
    return jsonify([difficulty.to_dict() for difficulty in difficulties])

def get_difficulty(id):
    difficulty = Difficulty.query.get(id)
    if not difficulty:
        return jsonify({'error': 'Difficulty not found'}), 404
    return jsonify(difficulty.to_dict())

def add_difficulty():
    new_difficulty_data = request.get_json()
    new_difficulty = Difficulty(
        name=new_difficulty_data['name']
    )
    db.session.add(new_difficulty)
    db.session.commit()
    return jsonify({'message': 'difficulty added successfully!', 'category': new_difficulty.to_dict()}), 201

def update_difficulty(id):
    difficulty = Difficulty.query.get(id)
    if not difficulty:
        return jsonify({'error': 'Difficulty not found'}), 404
    updated_data = request.get_json()
    difficulty.name = updated_data.get('name', difficulty.name)
    db.session.commit()
    return jsonify({'message': 'Difficulty updated successfully!', 'difficulty': difficulty.to_dict()})

def delete_difficulty(id):
    difficulty = Difficulty.query.get(id)
    if not difficulty:
        return jsonify({'error': 'Difficulty not found'}), 404
    db.session.delete(difficulty)
    db.session.commit()
    return jsonify({'message': 'Difficulty deleted successfully!'})