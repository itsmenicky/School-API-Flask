from flask import Flask
from config import myApp, db
from ActivityController.ActivityController import activities_blueprint

def create_app():
    # Inicializa a aplicação Flask
    app = myApp

    # Registra os blueprints
    app.register_blueprint(activities_blueprint)

    # Cria o banco de dados apenas no contexto da aplicação
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])