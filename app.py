from flask import Flask
from config import myApp, db
from controllers.teacherController import teachers_blueprint
from controllers.classroomController import classes_blueprint
from controllers.studentController import students_blueprint

def create_app():
    # Inicializa a aplicação Flask
    app = myApp

    # Registra os blueprints
    app.register_blueprint(teachers_blueprint)
    app.register_blueprint(classes_blueprint)
    app.register_blueprint(students_blueprint)

    # Cria o banco de dados apenas no contexto da aplicação
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])

#Adicionando linha para testar o workflow
