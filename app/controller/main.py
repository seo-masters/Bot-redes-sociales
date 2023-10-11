import random
import time
import requests
from models.facebook_api import FacebookAPI
from models.openai_api import OpenAIClient
from models.pexels_api import PexelsAPI
from models.api.credentials import Get_credentials
from controller.control_browser_facebook import Control_facebook
from models.pixabay_api import PixabayAPI


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
        facebook = FacebookAPI()
        rta = facebook.authenticate_facebook()
        return rta

    def madurar_perfil(self, respuesta_queue):
        
        #bot = Control_facebook("camilarodriguez5254@hotmail.com","C1234567R")
        #rta = bot.facebook_main()
        time.sleep(1)
        respuesta_queue.put(f"Hola mundo {random.randint(1, 100)}")

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
        photo2 = PixabayAPI()

        data = Get_credentials()
        keys = data.get_users_facebook("qpodqrba2at0mek")
        key_word = keys["key_word"]
        print(keys["name"])

        post_img = openai_client.chatGpt(
            input=f"**Dame un mensaje para un post en facebook utiliza alguna de estas palabras -no mezcles todas las palabras- maximo 30 palabras: {key_word}**"
        )
        titulo_img = openai_client.chatGpt(
            f"Por favor, dame solo 2 palabras relacionadas: en ingles {post_img}"
        )
        print(f"buscando imagenes: {titulo_img}")
        # sucess, img_url = photo.search_photo(titulo_img)
        titulo_img = titulo_img.replace("[^a-zA-Z0-9]", "").replace(",", "")

        sucess, img_url = photo2.get_images(titulo_img)
        print(img_url)

        if sucess:
            imagen_url = self.download_image_url(img_url, "photo.jpg")
            # Publica la imagen en la página de Facebook
            facebook = FacebookAPI(keys["access_token"])
            access_token = facebook.facebook_post(keys["page_id"], post_img, imagen_url)
            print(access_token)
        # Descarga la imagen de la URL especificada
        else:
            return img_url

    def download_image_url(self, url, filename):
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename

    def chat_gpt(self, prompt):
        ia = OpenAIClient("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")
        return ia.camila_chatbot(prompt,"soy un perro mi nombre es bruno")
