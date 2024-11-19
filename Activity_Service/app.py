from config import create_app
from ActivityController.ActivityController import activity_bp

app = create_app()
app.register_blueprint(activity_bp, url_prefix='/activity')

if __name__ == '__main__':
    app.run(host='localhost', port=5002)