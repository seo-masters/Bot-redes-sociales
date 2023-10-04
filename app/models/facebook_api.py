import facebook
import requests


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


    def get_facebook_code(app_id="726809776152575", redirect_uri="http://localhost:8080/callback"):
        # Create the request URL.
        url = "https://www.facebook.com/v13.0/dialog/oauth/?"
        params = {
            "client_id": app_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
        }

        # Make the request.
        response = requests.get(url, params=params)

        # Check the response status code.
        if response.status_code == 200:
            # The code was obtained successfully.
            return response.url.split("code=")[-1]
        else:
            # An error occurred.
            raise ValueError(
                f"An error occurred while obtaining the code. Status code: {response.status_code}"
            )

