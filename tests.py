import unittest
import json
from app import db, create_app
from models.classroomModel import Classroom
from models.studentModel import Student
from models.teacherModel import Teacher

class ModelTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Cria a aplicação e o contexto
        cls.app = create_app()
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usando banco de dados em memória
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()  # Cria as tabelas

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()  # Remove todas as tabelas
        cls.app_context.pop()

    def setUp(self):
        # Cria um novo banco de dados para cada teste
        db.create_all()

    def tearDown(self):
        # Limpa a sessão e remove as tabelas após cada teste
        db.session.remove()
        db.drop_all()

    #Teste de criação de um professor
    def test_teacher_creation(self):
        teacher = Teacher('Maria', 40, 'Matemática', 'Ótima professora')
        db.session.add(teacher)
        db.session.commit()
        
        # Verifica se o professor foi criado corretamente
        self.assertEqual(teacher.nome, 'Maria')
        self.assertEqual(teacher.id, 1)

    #Teste de criação e atualização de um professor
    def test_teacher_creation_and_update(self):
        teacher = Teacher('João Almeida', 35, 'História', 'Professor com dupla personalidade')
        db.session.add(teacher)
        db.session.commit()

        #Requisição JSON para atualização de um professor
        json_data = '''{
                "materia":"Lógica de Programação"
                }'''
        
        #Transformando a requisição JSON em dicionário
        new_data = json.loads(json_data)

        #Atualizando o professor criado
        Teacher.update_teacher(teacher.id, new_data)
        db.session.commit()

        self.assertEqual(teacher.materia, "Lógica de Programação")

    #Teste de criação de uma turma com a criação de um professor
    def test_classroom_creation_with_teacher(self):
        teacher = Teacher('João', 35, 'História', 'Ótimo professor')
        db.session.add(teacher)
        db.session.commit()

        classroom = Classroom('classroom A', teacher.id, 'Sim')
        db.session.add(classroom)
        db.session.commit()

        # Verifica se a sala de aula foi criada com o professor correto
        self.assertEqual(classroom.professor.nome, 'João')

    #Teste de criação e atualização de uma turma
    def test_classroom_creation_and_update(self):
        #Criação de um professor
        teacher = Teacher('Mário', 45, 'Sociologia', 'Professor muito falastrão')
        db.session.add(teacher)
        db.session.commit()

        #Criação de uma turma
        classroom = Classroom('classroom B', teacher.id, 'Sim')
        db.session.add(classroom)
        db.session.commit()

        #Requisição JSON para a atualização de uma turma
        json_data = '''{
                "descricao":"classroom C"}'''
        
        #Transformando a requisição JSON em dicionário
        new_data = json.loads(json_data)

        #Atualização da turma no banco de dados
        Classroom.update_classroom(classroom.id, new_data)
        db.session.commit()

    #Teste de criação de um estudante com uma turma
    def test_student_creation_with_classroom(self):
        #Criando professor
        teacher = Teacher('Ana', 30, 'Química', 'Muito teórica')
        db.session.add(teacher)
        db.session.commit()

        #Criando turma
        classroom = Classroom('classroom B', teacher.id, 'Sim')
        db.session.add(classroom)
        db.session.commit()

        #Criando estudante
        student = Student('Carlos', 15, classroom.id, 
                          '2008-05-15', 7.5, 8.0)
        db.session.add(student)
        db.session.commit()

        # Verifica se o aluno foi criado na sala de aula correta
        self.assertEqual(student.turma.descricao, 'classroom B')
        self.assertAlmostEqual(student.media_final, 7.75)

    #Teste de criação de um estudante e atualização
    def test_student_creation_and_update(self):
        #Criando um professor
        teacher = Teacher('Ana Júlia', 45, 'Filosofia', 'Tem uma música dela')
        db.session.add(teacher)
        db.session.commit()

        #Criando uma turma
        classroom = Classroom('classroom 45', teacher.id, 'Sim')
        db.session.add(classroom)
        db.session.commit()

        #Criando um estudante
        student = Student('Vitória', 18, classroom.id, '2006-09-11', 7.5, 9.0)
        db.session.add(student)
        db.session.commit()

        #Requisição JSON para atualizar um usuário
        json_data = '''{
                "nome":"Vitória Silva"}'''
        
        #Transformando requisição JSON em dicionário 
        new_data = json.loads(json_data)

        #Atualizando o estudante
        Student.update_student(student.id, new_data)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
