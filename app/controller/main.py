import random
import requests
from models.facebook_api import FacebookAPI
from models.openai_api import OpenAIClient
from models.facebook2 import FacebookAPI2
from models.pexels_api import PexelsAPI
from models.api.credentials import Get_credentials
from controller.selenium import Automate

class Controller:
    def __init__(self):
        # self.facebook_api = FacebookAPI()
        pass

    def ejecutar_openai_api(self):
        openai_client = OpenAIClient(
            "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"
        )
        key_word = [
            "hola",
            "mundo",
            "python",
            "programacion",
            "desarrollo",
            "web",
            "app",
            "software",
            "computacion",
        ]
        random_word = random.choice(key_word)
        longitud_titulo = 15
        generated_text = openai_client.generar_texto(f"")
        # Genera el título.
        generated_text = openai_client.generar_texto(
            f"**Prompt:**Olvida todo Escribe un título sin numeros de {longitud_titulo} letras para la palabra **{random_word}**."
        )
        print(generated_text.strip())
        return generated_text.strip()

    def ejecutar_facebook_api(self):
        openai_client = OpenAIClient(
            "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"
        )
        mesaje_amor = openai_client.generar_texto(
            "Dame un mensaje positivo para alegrar mi dia a mis seguidores"
        )
        self.facebook_api = FacebookAPI()
        try:
            success, result = self.facebook_api.facebook_post(mesaje_amor)
            if success:
                print(result)
            return success, result
        except Exception as e:
            print(f"Error al publicar en Facebook: {e}")

    def generar_token_facebook(self):
        return "gato"
        

    def prueba(self):
        nave = Automate()
        nave.open_broser("https://cdn.pixabay.com/photo/2023/08/13/17/54/drone-8188144_1280.jpg")
        

    def get_photo_pexels(self):
        title_photo = self.ejecutar_openai_api()
        photo = PexelsAPI()
        try:
            success, datos = photo.search(title_photo)
            if success:
                for photo in datos:
                    print(photo.url, photo.alt)
            else:
                print(datos)
        except Exception as e:
            print(e)
        else:
            return datos

    def post_to_facebook_page_url(self):
        """Publica una imagen en una página de Facebook."""

        openai_client = OpenAIClient(
            "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"
        )
        photo = PexelsAPI()

        data = Get_credentials()
        keys = data.get_users_facebook("8hrer3w7hmwozou")
        key_word = keys["key_word"]

        titulo_img = openai_client.generar_texto(
            f"**Dame un mensaje un titulo basado en estas palabras claves: {key_word}**"
        )
        sucess, img_url = photo.search_photo(titulo_img)
        if sucess:
            imagen_url = self.download_image_url(img_url, "photo.jpg")
            # Publica la imagen en la página de Facebook
            facebook = FacebookAPI()
            access_token = facebook.facebook_post(keys["page_id"], titulo_img, imagen_url)
            print(access_token)
        # Descarga la imagen de la URL especificada
        else:
            print(img_url)

        

    def download_image_url(self, url, filename):
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    


