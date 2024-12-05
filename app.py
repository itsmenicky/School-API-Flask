from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from config import myApp, db
from controllers.teacherController import teachers_blueprint
from controllers.classroomController import classes_blueprint
from controllers.studentController import students_blueprint

### Swagger UI ###
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)

def create_app():
    # Inicializa a aplicação Flask
    app = myApp

    # Registra os blueprints
    app.register_blueprint(teachers_blueprint)
    app.register_blueprint(classes_blueprint)
    app.register_blueprint(students_blueprint)
    app.register_blueprint(swaggerui_blueprint)

    # Cria o banco de dados apenas no contexto da aplicação
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
