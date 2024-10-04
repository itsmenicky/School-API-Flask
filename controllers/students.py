from flask import Blueprint, jsonify, request
from models.student import Student
from dal.db import students

students_blueprint = Blueprint('students', __name__)

# Exemplo de como poderia ficar o cadastro após adicionar os models
#Cadastrando um aluno
@students_blueprint.route('/students', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student.add_student(data)
    return jsonify(new_student.to_dict()), 201


#Resgatando alunos cadastrados
@students_blueprint.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

#Atualizando dados de um aluno
@students_blueprint.route('/students/<int:student_id>', methods=['PUT'])
def update_students(student_id):
    for student in students:
        if student['id'] == student_id:
            data = request.json
            student["nome"] = data.get('nome', student['nome'])
            student["idade"] = data.get('idade', student['idade'])
            student["materia"] = data.get('materia', student['materia'])
            student["observacoes"] = data.get('observacoes', student['observacoes'])
            return jsonify(student), 201
              
    return jsonify({"ERRO":"Aluno não encontrado!"}), 404

#Deletando um professor
@students_blueprint.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({"mensagem":"Usuário deletado com sucesso!"}), 201
    return jsonify({"ERRO":"Usuário não encontrado!"}), 404
