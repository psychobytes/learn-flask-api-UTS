from flask import Blueprint
from controllers.MachineController import get_machines, get_machine, add_machine, update_machine, patch_machine, delete_machine

machine_bp = Blueprint('Machine_bp', __name__)

machine_bp.route('/api/machine', methods=['GET'])(get_machines)
machine_bp.route('/api/machine/<int:machine_id>', methods=['GET'])(get_machine)
machine_bp.route('/api/machine', methods=['POST'])(add_machine)
machine_bp.route('/api/machine/<int:machine_id>', methods=['PATCH'])(patch_machine)
machine_bp.route('/api/machine/<int:machine_id>', methods=['PUT'])(update_machine)
machine_bp.route('/api/machine/<int:machine_id>', methods=['DELETE'])(delete_machine)