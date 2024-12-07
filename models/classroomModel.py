from config import db 
from models.teacherModel import Teacher, TeacherNotFound

class Classroom(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(120))
    professor_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # chave estrangeira
    professor = db.relationship('Teacher', backref='classes')  # relação com a classe Teacher
    ativo = db.Column(db.String(15))

    def __init__(self, descricao, professor_id, ativo):
        # Inicializa um objeto da classe Classroom com os atributos id, descricao, professor e ativo
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        # Converte o objeto Classroom para um dicionário
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor": self.professor.to_dict(),
            "ativo": self.ativo
        }

    @staticmethod
    def get_all():
        classes = Classroom.query.all()
        return [classroom.to_dict() for classroom in classes]


    @staticmethod
    def get_by_id(classroom_id):
       classroom = Classroom.query.get(classroom_id)
       if not classroom:
           raise ClassroomNotFound
       return classroom.to_dict()
           

    @staticmethod
    def add_classroom(classroom_data):
        # Cria um novo aluno com os dados fornecidos, atribuindo um novo ID
        teacher = Teacher.query.get(classroom_data['professor_id'])
        if not teacher:
            raise TeacherNotFound
        else:
            classroom = Classroom(classroom_data['descricao'], 
                            teacher.id, 
                            classroom_data['ativo'])
            db.session.add(classroom)
            db.session.commit()

    @staticmethod
    def update_classroom(classroom_id, new_data):
        classroom = Classroom.query.get(classroom_id)
        if not classroom:
            raise ClassroomNotFound
        else:
            if 'descricao' in new_data:
                classroom.descricao = new_data['descricao']
            elif 'professor_id' in new_data:
                teacher = Teacher.query.get(new_data['professor_id'])
                if not teacher:
                    raise TeacherNotFound
                else:
                    classroom.professor_id = new_data['professor_id']
            elif 'ativo' in new_data:
                classroom.ativo = new_data['ativo']
        db.session.commit()

    @staticmethod
    def delete_classroom(classroom_id):
        classroom = Classroom.query.get(classroom_id)
        if not classroom:
            raise ClassroomNotFound
        db.session.delete(classroom)
        db.session.commit()

class ClassroomNotFound(Exception):
        pass