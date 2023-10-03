import facebook

class FacebookAPI2:
    def __init__(self, app_id, app_secret):
        self.access_token = facebook.GraphAPI(app_id, app_secret).access_token
        self.graph = facebook.GraphAPI(access_token=self.access_token)


    def publicar_en_muro(self, message):
        try:
            print(self.access_token)
            # Realiza la solicitud POST para publicar en el muro
            self.graph.put_object("me", "feed", message=message)
            return True, "Publicación realizada con éxito."
        except facebook.GraphAPIError as e:
            print(f"Error al publicar en el muro: {e}")
            return False, f"Error al publicar en el muro: {e}"