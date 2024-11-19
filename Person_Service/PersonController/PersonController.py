from flask import Blueprint, jsonify
from PersonModel import PersonModel

person_bp = Blueprint('person_bp', __name__)

@pessoa_bp.route('/teachers', methods=['GET'])
def list_teachers():
    teachers = PersonModel.list_teachers()
    return jsonify(teachers)

@person_bp.route('/students', methods=['GET'])
def list_students():
    students = PersonModel.list_students()
    return jsonify(students)

@person_bp.route('/teaches/<int:teacher_id>/<int:id_discipline>', methods=['GET'])
def verify_teaches(teacher_id, id_discipline):
    try:
        teaches = PersonModel.teaches(teacher_id, id_discipline)
        return jsonify({'teaches': teaches})
    except PersonModel.DisciplineNotFound:
        return jsonify({'error': 'Discipline not found'}), 404