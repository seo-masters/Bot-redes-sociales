import facebook

class FacebookAPI:
    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token)

    def publicar_en_muro(self, message):
        try:
            # Realiza la solicitud POST para publicar en el muro
            self.graph.put_object("me", "feed", message=message)
            return True, "Publicación realizada con éxito."
        except facebook.GraphAPIError as e:
            return False, f"Error al publicar en el muro: {e}"

