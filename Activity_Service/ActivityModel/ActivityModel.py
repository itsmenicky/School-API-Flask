from config import db

class Activity(db.Model):
    __tablename__ = 'activities'

    id_atividade = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(255), nullable=False)
    respostas = db.Column(db.JSON, nullable=True)  # Lista de respostas

    def __init__(self, id_disciplina, enunciado, respostas=None):
        self.id_disciplina = id_disciplina
        self.enunciado = enunciado
        self.respostas = respostas if respostas is not None else []

    def to_dict(self):
        return {
            "id_atividade": self.id_atividade,
            "id_disciplina": self.id_disciplina,
            "enunciado": self.enunciado,
            "respostas": self.respostas
        }

    @staticmethod
    def get_all():
        activities = Activity.query.all()
        return [activity.to_dict() for activity in activities]

    @staticmethod
    def get_by_id(activity_id):
        activity = Activity.query.get(activity_id)
        if not activity:
            raise ActivityNotFound
        return activity.to_dict()

    @staticmethod
    def add_activity(activity_data):
        activity = Activity(
            id_disciplina=activity_data['id_disciplina'],
            enunciado=activity_data['enunciado'],
            respostas=activity_data.get('respostas', [])
        )
        db.session.add(activity)
        db.session.commit()

    @staticmethod
    def update_activity(activity_id, new_data):
        activity = Activity.query.get(activity_id)
        if not activity:
            raise ActivityNotFound
        activity.id_disciplina = new_data['id_disciplina']
        activity.enunciado = new_data['enunciado']
        activity.respostas = new_data['respostas']
        db.session.commit()

    @staticmethod
    def delete_activity(activity_id):
        activity = Activity.query.get(activity_id)
        if not activity:
            raise ActivityNotFound
        db.session.delete(activity)
        db.session.commit()

class ActivityNotFound(Exception):
    pass