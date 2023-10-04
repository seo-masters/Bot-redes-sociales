import requests
import json

class PexelsAPI:
    def __init__(
        self, api_key="5gmdoXnZ0LOjI9ie27rQmubggwzaUTxLpaf5zMhZi0BgkYU8BtmGtT2U"
    ):
        self.api_key = api_key
        self.api_url = "https://api.pexels.com/v1/"

    def search(self, query, per_page=10, page=1):
        headers = {
            "Authorization": f"OtGxtBEsqhLx8gO4kbbbEQfrJsvSRbTNKXRIFrgxhMFpK8IOnCz4I2Rg"
        }

        response = requests.get(
            f"{self.api_url}/search?query={query}&per_page={per_page}&page={page}",
            headers=headers
        )
        print("hola ", response)

        try:
            data = response.json()
            return [Photo(photo) for photo in data["photos"]]
        except (json.JSONDecodeError, requests.HTTPError) as e:
            if e.status_code != 200:
                print(f"Error de la API: {e.status_code}")
                raise ValueError(f"Error de la API: {e.status_code}")




class Photo:
    def __init__(self, data):
        self.id = data["id"]
        self.url = data["url"]


# if __name__ == "__main__":
#     # Obtén tu clave API de Pexels.
#     api_key = "5gmdoXnZ0LOjI9ie27rQmubggwzaUTxLpaf5zMhZi0BgkYU8BtmGtT2U"

#     # Crea un objeto PexelsAPI.
#     pexels = PexelsAPI(api_key)

#     # Realiza una consulta de búsqueda.
#     search_results = pexels.search("gatos")

#     # Imprime los resultados de la consulta.
#     for photo in search_results:
#         print(photo.id, photo.url)
