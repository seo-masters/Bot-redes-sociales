import random
from models.facebook_api import FacebookAPI
from models.openai_api import OpenAIClient
from models.facebook2 import FacebookAPI2
from models.pexels_api import PexelsAPI


class Controller:
    def __init__(self):
        #self.facebook_api = FacebookAPI()
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
        mesaje_amor = openai_client.generar_texto("Dame un mensaje positivo para alegrar mi dia a mis seguidores")
        self.facebook_api = FacebookAPI() 
        try:
            success, result = self.facebook_api.publicar_en_muro(mesaje_amor)
            if success:
                print(result)
            return success, result
        except Exception as e:
            print(f"Error al publicar en Facebook: {e}")

    def generar_token_facebook(self):
        facebook_3 = FacebookAPI2(
            "149414758247584",
            "0d235772323370d051639fab3b59bbd5",
            "EAAKVB5aG3ZC8BO23zrQFjix4cIDDMj1fgRqmuOBlQmRnuYlph6STjHAI9xuonIczsixnl8jj8WdNwxbC7K0eArpSZBxlSpz3jnBQsDgSmK9ZCQxsAAazdpInHCUiQYhJjBi9GYuiOXFjtia4IASHpWHWMgk2GXNTSV5XQkXJLZAZCBxacbZAuILavrqt3XgBN2rwYUzaBmfJZBPAB3ZAAhMSfZBcXEwZDZD",
        )
        self.facebook_3 = facebook_3

    def prueba(self):
        print(f"Prueba con argumento")

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

    def post_to_facebook_page(self):
        #application_id = "726809776152575"# Peliculas Api
        #app_secret_key = "0d235772323370d051639fab3b59bbd5"
        facebook = FacebookAPI()
        try:
            
            access_token = facebook.facebook_post_photo()

            #access_token = facebook.get_facebook_code(application_id,app_secret_key)
            #rta = facebook.facebook_post_me("149414758247584", "Dura 3 meses", access_token)
            rta2 = facebook.facebook_post_photo_from_url("149414758247584","https://images.pexels.com/photos/6590699/pexels-photo-6590699.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=200&w=280")
            print(rta2)
        except Exception as e:
            print(e)
