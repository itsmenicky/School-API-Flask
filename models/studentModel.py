from config import db
from models.classroomModel import Classroom, ClassroomNotFound

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120))
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    turma = db.relationship('Classroom', backref='students') 
    data_nascimento = db.Column(db.String)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        # Inicializa um objeto da classe Aluno
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id  # Relaciona Aluno a uma turma
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcular_media()

    def to_dict(self):
        # Converte o objeto Aluno para um dicionário para facilitar a serialização
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma": self.turma.to_dict(),  # ID da turma do aluno
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.calcular_media()
        }

    def calcular_media(self):
        # Calcula a média final do aluno com base nas notas dos dois semestres
        return (float(self.nota_primeiro_semestre) + float(self.nota_segundo_semestre)) / 2

    @staticmethod
    def get_all():
        students = Student.query.all()
        return [student.to_dict() for student in students]

    @staticmethod
    def get_by_id(student_id):
        student = Student.query.get(student_id)
        if not student:
            raise StudentNotFound
        return student.to_dict()


    @staticmethod
    def add_student(student_data):
        # Cria um novo aluno com os dados fornecidos, atribuindo um novo ID
        classroom = Classroom.query.get(student_data['turma_id'])
        if not classroom:
            raise ClassroomNotFound
        else:
            student = Student(student_data['nome'], 
                            student_data['idade'], 
                            classroom.id, 
                            student_data['data_nascimento'], 
                            student_data['nota_primeiro_semestre'], 
                            student_data['nota_segundo_semestre'])
            db.session.add(student)
            db.session.commit()

    @staticmethod
    def update_student(student_id, new_data):
        student = Student.query.get(student_id)
        if not student:
            raise StudentNotFound
        else:
            if 'nome' in new_data:
                student.nome = new_data['nome']
            elif 'idade' in new_data:
                student.idade = new_data['idade']
            elif 'turma_id' in new_data:
                classroom = Classroom.query.get(new_data['turma_id'])
                if not classroom:
                    raise ClassroomNotFound
                else:
                    student.turma_id = new_data['turma_id']
            elif 'data_nascimento' in new_data:
                student.data_nascimento = new_data['data_nascimento']
            elif 'nota_primeiro_semestre' in new_data:
                student.nota_primeiro_semestre = new_data['nota_primeiro_semestre']
            elif 'nota_segundo_semestre' in new_data:
                student.nota_segundo_semestre = new_data['nota_segundo_semestre']

        db.session.commit()

    @staticmethod
    def delete_student(student_id):
        student = Student.query.get(student_id)
        if not student:
            raise StudentNotFound
        db.session.delete(student)
        db.session.commit()
       
       
class StudentNotFound(Exception):
        pass
