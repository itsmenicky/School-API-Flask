import requests

PERSON_SERVICE_URL = "http://localhost:5001/people"

class PersonServiceClient:
    @staticmethod
    def verify_teaches(teacher_id, id_discipline):
        url = f"{PERSON_SERVICE_URL}/teaches/{teacher_id}/{id_discipline}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('teaches', False) if data.get('isok') else False
        except requests.RequestException as e:
            print(f"Error accessing person service: {e}")
            return False