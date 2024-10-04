from dal.db import classes
from dal.db import students   

class Student:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        # Inicializa um objeto da classe Aluno
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id  # Relaciona Aluno a uma turma
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre

    def to_dict(self):
        # Converte o objeto Aluno para um dicionário para facilitar a serialização
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,  # ID da turma do aluno
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.calcular_media()
        }

    def calcular_media(self):
        # Calcula a média final do aluno com base nas notas dos dois semestres
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    @staticmethod
    def get_all():
        # Retorna todos os alunos na lista 'alunos', criando instâncias de Aluno
        return [Student(**student) for student in students]

    @staticmethod
    def get_by_id(student_id):
        # Busca um aluno pelo ID na lista 'alunos'
        for student in students:
            if student["id"] == student_id:
                return Student(**student)
        return None  # Retorna None se o aluno não for encontrado

    @staticmethod
    def add_student(student_data):
        # Cria um novo aluno com os dados fornecidos, atribuindo um novo ID
        new_student = {
            "id": len(students) + 1,
            "nome": student_data['nome'],
            "idade": student_data['idade'],
            "turma_id": student_data['turma_id'],  # Associa o aluno a uma turma
            "data_nascimento": student_data['data_nascimento'],
            "nota_primeiro_semestre": student_data['nota_primeiro_semestre'],
            "nota_segundo_semestre": student_data['nota_segundo_semestre']
        }
        students.append(new_student)
        return Student(**new_student)

    @staticmethod
    def update_student(student_id, data):
        # Atualiza os dados de um aluno existente pelo ID
        for student in students:
            if student['id'] == student_id:
                student['nome'] = data.get('nome', student['nome'])
                student['idade'] = data.get('idade', student['idade'])
                student['turma_id'] = data.get('turma_id', student['turma_id'])
                student['data_nascimento'] = data.get('data_nascimento', student['data_nascimento'])
                student['nota_primeiro_semestre'] = data.get('nota_primeiro_semestre', student['nota_primeiro_semestre'])
                student['nota_segundo_semestre'] = data.get('nota_segundo_semestre', student['nota_segundo_semestre'])
                return Student(**student)
        return None

    @staticmethod
    def delete_student(student_id):
        # Remove um aluno da lista 'alunos' pelo ID
        global students  # Acessa a lista global 'alunos'
        students = [student for student in students if student["id"] != student_id]
