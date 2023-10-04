import facebook
import requests


class FacebookAPI:
    def __init__(self, access_token="EAAKVB5aG3ZC8BOZBSpKYXbUD44KCuPk4WZCRWoYjw7ZCVp6izPBgMV14HBOZBEQtI7ScOLwzJqqB3mVtZCZArEN2qViNvJDZAVzDhs4pzlxU9uKEZC259ZB93Gk4ZAkTH4ReZAp6ZBancZBd7d35msNsLhAzCJgTZBiZCPyGZACUcHyE5rOBRiZB2WvuufrMlck4q0NGLKA15GkTMlwRQZD"):
        self.access_token = access_token
        

    def publicar_en_muro(self, message):
        try:
            # Realiza la solicitud POST para publicar en el muro
            graph = facebook.GraphAPI("EAAKVB5aG3ZC8BOZBSpKYXbUD44KCuPk4WZCRWoYjw7ZCVp6izPBgMV14HBOZBEQtI7ScOLwzJqqB3mVtZCZArEN2qViNvJDZAVzDhs4pzlxU9uKEZC259ZB93Gk4ZAkTH4ReZAp6ZBancZBd7d35msNsLhAzCJgTZBiZCPyGZACUcHyE5rOBRiZB2WvuufrMlck4q0NGLKA15GkTMlwRQZD")

            graph.put_object("me", "feed", message=message)
            return True, "Publicación realizada con éxito."
        except facebook.GraphAPIError as e:
            return False, f"Error al publicar en el muro: {e}"


    def get_facebook_code(self, client_id, client_secret):
        try:
            oauth_access_token = facebook.GraphAPI().get_app_access_token(client_id, client_secret)
            print(f"Codigo OK {oauth_access_token}")
            return oauth_access_token
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                print("El código de autorización es inválido.")
            elif e.response.status_code == 500:
                print("Hay un error interno en el servidor de Facebook.")
            else:
                print(e)

            # Ahora tienes un token de acceso de aplicación
            print("Token de acceso de aplicación:", oauth_access_token)
            

    def facebook_post_me(self, page_id, message, access_token):
        #access_token = '726809776152575|y9Ej7bC-vDXvE8lvti28Qkd4q5o'
        # Crea una instancia del objeto de la API de Facebook
        graph = facebook.GraphAPI("EAAKVB5aG3ZC8BOZBSpKYXbUD44KCuPk4WZCRWoYjw7ZCVp6izPBgMV14HBOZBEQtI7ScOLwzJqqB3mVtZCZArEN2qViNvJDZAVzDhs4pzlxU9uKEZC259ZB93Gk4ZAkTH4ReZAp6ZBancZBd7d35msNsLhAzCJgTZBiZCPyGZACUcHyE5rOBRiZB2WvuufrMlck4q0NGLKA15GkTMlwRQZD")

        # Publica el mensaje en la página
        try:
            rta = graph.put_object(page_id, "feed", message=message)
            print("Mensaje publicado con éxito en la página.")
            return rta
        except facebook.GraphAPIError as e:
            print("Ocurrió un error al publicar el mensaje:", e)


    def facebook_post_photo(self, page_id, photo_file, access_token):
        # Crea una instancia del objeto de la API de Facebook
        graph = facebook.GraphAPI("EAAKVB5aG3ZC8BOZBSpKYXbUD44KCuPk4WZCRWoYjw7ZCVp6izPBgMV14HBOZBEQtI7ScOLwzJqqB3mVtZCZArEN2qViNvJDZAVzDhs4pzlxU9uKEZC259ZB93Gk4ZAkTH4ReZAp6ZBancZBd7d35msNsLhAzCJgTZBiZCPyGZACUcHyE5rOBRiZB2WvuufrMlck4q0NGLKA15GkTMlwRQZD")

        # Carga la foto en la página
        try:
            rta = graph.put_photo(page_id, photo_file)
            print("Foto cargada con éxito en la página.")
            return rta
        except facebook.GraphAPIError as e:
            print("Ocurrió un error al cargar la foto:", e)


    def facebook_post_photo_from_url(self, page_id, photo_url):
        # Crea una instancia del objeto de la API de Facebook
        print(photo_url)
        graph = facebook.GraphAPI(self.access_token)

        # Carga la foto desde la URL
        photo_file = requests.get(photo_url).content

        # Carga la foto en la página
        try:
            rta = graph.put_photo(page_id, photo_file)
            print("Foto cargada con éxito en la página.")
            return rta
        except facebook.GraphAPIError as e:
            print("Ocurrió un error al cargar la foto:", e)
