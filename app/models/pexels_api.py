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

        try:
            response = requests.get(
                f"{self.api_url}/search?query={query}&per_page={per_page}&page={page}",
                headers=headers,
            )
            if response.status_code == 200:
                data = response.json()
                return True, [Photo(photo) for photo in data["photos"]]
            else:
                return False, "status_code " + str(response.status_code)
            
        except Exception  as e:
            print(f"Error: {e}")
            raise ValueError(f"Error: {e}")
        
    def search_photo(self, query):
        headers = {
            "Authorization": f"jt4Uw37OAnj8TFG9yfY9AUHwklT37OsrKXqLqHGUg1knsCOQV1agygd9"
        }

        try:
            response = requests.get(
                f"{self.api_url}/search?query={query}&per_page=1&page=1",
                headers=headers,
            )
            print(response)
            if response.status_code == 200:
                data = response.json()
                photo = data['photos'][0]['src']['original']
                print(photo)
                return True, photo
            else:
                return False, "search_photo: status_code " + str(response.status_code)
            
        except Exception  as e:
            print(f"Error: {e}")
            raise ValueError(f"Error: {e}")



class Photo:
    def __init__(self, data):
        self.id = data["id"]
        self.url = data["url"]
        self.alt = data["alt"]
