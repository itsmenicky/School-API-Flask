from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from ActivityModel.ActivityModel import Activity, ActivityNotFound

activities_blueprint = Blueprint('activities', __name__)

@activities_blueprint.route('/atividades/', methods=['POST'])
def create_activity():
    new_activity = {
        'id_disciplina': request.json['id_disciplina'],
        'enunciado': request.json['enunciado'],
        'respostas': request.json.get('respostas', [])
    }
    Activity.add_activity(new_activity)
    return jsonify(Activity.get_all()), 201

@activities_blueprint.route('/atividades/<int:activity_id>/', methods=['PUT'])
def update_activity(activity_id):
    try:
        new_data = {
            'id_disciplina': request.json['id_disciplina'],
            'enunciado': request.json['enunciado'],
            'respostas': request.json['respostas']
        }
        Activity.update_activity(activity_id, new_data)
        return jsonify(Activity.get_by_id(activity_id))
    except ActivityNotFound:
        return jsonify({'message': 'Atividade não encontrada'}), 404

@activities_blueprint.route('/atividades/<int:activity_id>/', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        Activity.delete_activity(activity_id)
        return jsonify(Activity.get_all())
    except ActivityNotFound:
        return jsonify({'message': 'Atividade não encontrada'}), 404