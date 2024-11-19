from flask import Blueprint, jsonify
from ActivityModel import ActivityModel
from Clients.Client_service import PersonServiceClient

activity_bp = Blueprint('activity_bp', __name__)

@activity_bp.route('/', methods=['GET'])
def list_activities():
    activities = ActivityModel.list_activities()
    return jsonify(activities)

@activity_bp.route('/<int:id_activity>', methods=['GET'])
def get_activity(id_activity):
    try:
        activity = ActivityModel.get_activity(id_activity)
        return jsonify(activity)
    except ActivityModel.ActivityNotFound:
        return jsonify({'error': 'Activity not found'}), 404

@activity_bp.route('/<int:id_activity>/teacher/<int:teacher_id>', methods=['GET'])
def get_activity_for_teacher(id_activity, teacher_id):
    try:
        activity = ActivityModel.get_activity(id_activity)
        if not PersonServiceClient.verify_teaches(teacher_id, activity['id_discipline']):
            activity = activity.copy()
            activity.pop('response', None)
        return jsonify(activity)
    except ActivityModel.ActivityNotFound:
        return jsonify({'error': 'Activity not found'}), 404