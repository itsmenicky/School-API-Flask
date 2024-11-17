import unittest
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

    def test_teacher_creation(self):
        teacher = Teacher('Maria', 40, 'Matemática', 'Ótima professora')
        db.session.add(teacher)
        db.session.commit()
        
        # Verifica se o professor foi criado corretamente
        self.assertEqual(teacher.nome, 'Maria')
        self.assertEqual(teacher.id, 1)  # ID deve ser 1 para o primeiro professor

    def test_classroom_creation_with_teacher(self):
        teacher = Teacher('João', 35, 'História', 'Ótimo professor')
        db.session.add(teacher)
        db.session.commit()

        classroom = Classroom('classroom A', teacher.id, 'Sim')
        db.session.add(classroom)
        db.session.commit()

        # Verifica se a sala de aula foi criada com o professor correto
        self.assertEqual(classroom.professor.nome, 'João')

    def test_student_creation_with_classroom(self):
        teacher = Teacher('Ana', 30, 'Química', 'Muito teórica')
        db.session.add(teacher)
        db.session.commit()

        classroom = Classroom('classroom B', teacher.id, 'Sim')
        db.session.add(classroom)
        db.session.commit()

        student = Student('Carlos', 15, classroom.id, 
                          '2008-05-15', 7.5, 8.0)
        db.session.add(student)
        db.session.commit()

        # Verifica se o aluno foi criado na sala de aula correta
        self.assertEqual(student.turma.descricao, 'classroom B')
        self.assertAlmostEqual(student.media_final, 8)

if __name__ == '__main__':
    unittest.main()
