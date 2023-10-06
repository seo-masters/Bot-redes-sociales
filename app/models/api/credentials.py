import requests


class Get_credentials:
    def get_users_facebook(self, id_users_facebook=""):
        url = f"http://127.0.0.1:8090/api/collections/users_facebook/records/{id_users_facebook}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener datos de la API: {response.text}")
            return None


class data_facebook:
    def __init__(self, data):
        self.id = data["id"]
        self.url = data["url"]
        self.alt = data["alt"]
