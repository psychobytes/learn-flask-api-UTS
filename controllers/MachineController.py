from flask import jsonify, request
from models.MachineModel import Machine
from models.CategoryModel import Category
from models.DifficultyModel import Difficulty
from config import db

def get_machines():
    machines = Machine.query.all()
    machines_with_categories = []
    for machine in machines:
        # Ambil category & difficulty terkait dari machine
        category = Category.query.get(machine.category_id)
        difficulty = Difficulty.query.get(machine.difficulty_id)
        # Tambahkan detail buku beserta nama category
        machines_with_categories.append({
            'id': machine.id,
            'title': machine.title,
            'author': machine.author,
            'category_name': category.name if category else "No Category",
            'difficulty_name': difficulty.name if difficulty else "No Difficulty"
        })
    response = {
        'status': 'success',
        'data': {
            'machines': machines_with_categories
        },
        'message': 'machines retrieved successfully'
    }
    return jsonify(response), 200

def get_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if not machine:
        return jsonify({'status': 'error', 'message': 'Machine not found'}), 404
    # Ambil category & difficulty terkait dari machine
    category = Category.query.get(machine.category_id)
    difficulty = Difficulty.query.get(machine.difficulty_id)
    machine_data = {
        'id': machine.id,
        'title': machine.title,
        'author': machine.author,
        'category_name': category.name if category else "No Category",
        'difficulty_name': difficulty.name if difficulty else "No Difficulty"
    }
    response = {
        'status': 'success',
        'data': {
            'machine': machine_data
        },
        'message': 'Machine retrieved successfully'
    }
    return jsonify(response), 200

def add_machine():
    new_machine_data = request.get_json()
    new_machine = Machine(
        title=new_machine_data['title'],
        author=new_machine_data['author'],
        category_id=new_machine_data['category_id'], # relation ke tabel category
        difficulty_id=new_machine_data['difficulty_id'] # relation ke tabel difficulty
    )
    db.session.add(new_machine)
    db.session.commit()
    return jsonify({'message': 'Machine added successfully!', 'machine': new_machine.to_dict()}), 201

def update_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if not machine:
        return jsonify({'error': 'Machine not found'}), 404
    updated_data = request.get_json()
    machine.title = updated_data.get('title', machine.title)
    machine.author = updated_data.get('author', machine.author)
    machine.category_id = updated_data.get('category_id', machine.category_id)
    machine.difficulty_id = updated_data.get('difficulty_id', machine.difficulty_id)

    db.session.commit()
    return jsonify({'message': 'Machine updated successfully!', 'macmachine': machine.to_dict()})

def patch_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if not machine:
        return jsonify({'error': 'Machine not found'}), 404
    patch_data = request.get_json()
    if 'title' in patch_data:
        machine.title = patch_data['title']
    if 'author' in patch_data:
        machine.author = patch_data['author']
    if 'category' in patch_data:
        # pastikan kategori ada sebelum update
        category = Category.query.get(patch_data['category_id'])
        if category:
            machine.category_id = patch_data['category_id']
        else:
            return jsonify({'error': 'Category not found'}), 404
    if 'difficulty' in patch_data:
        # pastikan difficulty ada sebelum update
        difficulty = Difficulty.query.get(patch_data['difficulty_id'])
        if difficulty:
            machine.difficulty_id = patch_data['difficulty_id']
        else:
            return jsonify({'error': 'Difficulty not found'}), 404

    db.session.commit()
    return jsonify({'message': 'Machine partially updated successfully!', 'machine': machine.to_dict()})

def delete_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if not machine:
        return jsonify({'error': 'Machine not found'}), 404
    db.session.delete(machine)
    db.session.commit()
    return jsonify({'message': 'Machine deleted successfully!'})