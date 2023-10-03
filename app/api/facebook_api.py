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

# Ejemplo de cómo usarlo
if __name__ == "__main__":
    # Token de acceso de Facebook
    access_token = 'tu_access_token'

    # Crea una instancia de la clase FacebookAPI
    facebook_api = FacebookAPI(access_token)

    # Mensaje que deseas publicar
    message = "Post Hecho con API Version 4"

    # Realiza la publicación en el muro
    success, message = facebook_api.publicar_en_muro(message)
    if success:
        print(message)
    else:
        print(message)
