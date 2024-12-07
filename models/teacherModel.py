from flask import jsonify
from config import db

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(120))
    observacoes = db.Column(db.String(120))

    def __init__(self, nome, idade, materia, observacoes):
        # Inicializa um objeto da classe Teacher com os atributos id, nome, idade, materia e observacoes
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        # Converte o objeto Teacher para um dicionário
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes
        }

    @staticmethod
    def get_all():
        teachers = Teacher.query.all()
        return [teacher.to_dict() for teacher in teachers]

    @staticmethod
    def get_by_id(teacher_id):
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise TeacherNotFound
        return teacher.to_dict()

    @staticmethod
    def add_teacher(teacher_data):
        # Cria um novo professor com os dados fornecidos, atribuindo um novo ID
        teacher = Teacher(teacher_data['nome'], 
                        teacher_data['idade'], 
                        teacher_data['materia'], 
                        teacher_data['observacoes'])
        db.session.add(teacher)
        db.session.commit()

    @staticmethod
    def update_teacher(teacher_id, new_data):
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            return TeacherNotFound
        elif 'nome' in new_data:
            teacher.nome = new_data['nome']
        elif 'idade' in new_data:
            teacher.idade = new_data['idade']
        elif 'materia' in new_data:
            teacher.materia = new_data['materia']
        elif 'observacoes' in new_data:
            teacher.observacoes = new_data['observacoes']
            
        db.session.commit()
        return jsonify({"SUCESSO":"PROFESSOR ATUALIZADO COM SUCESSO"}), 200

    @staticmethod
    def delete_teacher(teacher_id):
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            return TeacherNotFound
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({"SUCESSO":"PROFESSOR DELETADO COM SUCESSO"}), 200

class TeacherNotFound(Exception):
        pass
