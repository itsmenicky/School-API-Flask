teachers = [
    {'name': "joao", 'teacher_id': 1},
    {'name': "jose", 'teacher_id': 2},
    {'name': "maria", 'teacher_id': 3}
]

students = [
    {'name': "alexandre", 'student_id': 1},
    {'name': "miguel", 'student_id': 2},
    {'name': "janaina", 'student_id': 3},
    {'name': "cicero", 'student_id': 4},
    {'name': "dilan", 'student_id': 5}
]

disciplines = [
    {'name': "apis e microservicos", 'id_discipline': 1, 'students': [1, 2, 3, 4], 'teachers': [1], 'public': False},
    {'name': "matematica financeira", 'id_discipline': 2, 'students': [2], 'teachers': [3], 'public': True},
    {'name': "matematica básica", 'id_discipline': 3, 'students': [1, 2], 'teachers': [3, 2], 'public': False}
]

class DisciplineNotFound(Exception):
    pass

def list_teachers():
    return teachers

def list_students():
    return students

def teaches(teacher_id, id_discipline):
    for discipline in disciplines:
        if discipline['id_discipline'] == id_discipline:
            return teacher_id in discipline['teachers']
    raise DisciplineNotFound