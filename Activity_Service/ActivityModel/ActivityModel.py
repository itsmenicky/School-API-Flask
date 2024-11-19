activities = [
    {
        'id_activity': 1,
        'id_discipline': 1,
        'statement': 'Create a whole app in Flask',
        'response': [
            {'student_id': 1, 'response': 'all.py', 'nota': 9},
            {'student_id': 2, 'response': 'all.zip.rar'},
            {'student_id': 4, 'response': 'all.zip', 'nota': 10}
        ]
    },
    {
        'id_activity': 2,
        'id_discipline': 1,
        'statement': 'Crie um servidor que envia email em Flask',
        'response': [
            {'student_id': 4, 'response': 'email.zip', 'nota': 10}
        ]
    }
]

class ActivityNotFound(Exception):
    pass

def list_activities():
    return activities

def get_activity(id_activity):
    for activity in activities:
        if activity['id_activity'] == id_activity:
            return activity
    raise ActivityNotFound