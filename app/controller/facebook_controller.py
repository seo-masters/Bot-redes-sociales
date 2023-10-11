import random
import time

from models.facebook_api import FacebookAPI
from models.openai_api import OpenAIClient
from models.pexels_api import PexelsAPI
from models.api.credentials import Get_credentials
from controller.control_browser_facebook import Control_facebook

class Controller_facebook:
    def __init__(self):
        pass

    def madurar_perfil(self, respuesta_queue):

        try:
            data = Get_credentials()
            users = data.get_users_facebook()
            
            # Iterar sobre cada elemento en la lista asociada a la clave 'items'
            for item in users['items']:
                respuesta_queue.put("Ejecutando: "+item["nombre_de_campana"])
                # Acceder a las claves y valores dentro de cada elemento
                bot = Control_facebook(item, respuesta_queue)
                rta = bot.facebook_main()
                respuesta_queue.put(rta)
        except Exception as e:
            print(str(e))
            respuesta_queue.put("Error: " + str(e))

        

    
