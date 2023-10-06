import requests

class PixabayAPI:
    def __init__(self, api_key="39882404-cc38d8c08eb616db103ac7245"):
        self.api_key = api_key

    def get_images(self, query, per_page=10, page=10):
        url = f"https://pixabay.com/api/?key={self.api_key}&q={query}&page={page}&per_page={per_page}&lang=en"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"total fotos: {data['total']}")
            #print(f"total: {data['hits']}")
            if len(data["hits"]) > 0:
                return True, data["hits"][0]["webformatURL"]
            else:
                print("Sin resultados")
                return False, "PixabayAPI sin resultados en la busqueda"
        else:
            #raise Exception(f"Error al obtener imágenes: {response.status_code}")
            return False, f"Error al obtener imágenes: {response.status_code}"