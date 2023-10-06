import json
import facebook
import requests


class FacebookAPI:
    def __init__(
        self,
        access_token="EAAKVB5aG3ZC8BOZBSpKYXbUD44KCuPk4WZCRWoYjw7ZCVp6izPBgMV14HBOZBEQtI7ScOLwzJqqB3mVtZCZArEN2qViNvJDZAVzDhs4pzlxU9uKEZC259ZB93Gk4ZAkTH4ReZAp6ZBancZBd7d35msNsLhAzCJgTZBiZCPyGZACUcHyE5rOBRiZB2WvuufrMlck4q0NGLKA15GkTMlwRQZD",
    ):
        self.access_token = access_token

    def get_facebook_code(self, client_id, client_secret):
        try:
            oauth_access_token = facebook.GraphAPI().get_app_access_token(
                client_id, client_secret
            )
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


    def facebook_post(self, page_id, message, link_photo=None):
        # Crea una instancia del objeto de la API de Facebook
        graph = facebook.GraphAPI(self.access_token)

        if link_photo is not None:
            # Publica el mensaje en la página junto con las fotos
            try:
                local_photo = graph.put_photo(
                    image=open(link_photo, "rb"),
                    published=True,
                    album_path=page_id + "/photos",
                    message=message,
                )
                print("Foto y mensaje publicados con éxito en la página.")
                return local_photo["id"]
            except facebook.GraphAPIError as e:
                print("Error al publicar en la página de Facebook:", e)
        else:
            try:
                rta = graph.put_object(page_id, "feed", message=message)
                print("Mensaje publicado con éxito en la página.")
                return rta
            except facebook.GraphAPIError as e:
                print("Ocurrió un error al publicar el mensaje:", e)
