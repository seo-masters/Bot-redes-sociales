import facebook
import requests
import webbrowser
import http.server
import socketserver
import threading

class FacebookAPI:
    def __init__(
        self,
        access_token="EAAKVB5aG3ZC8BO6aJXsCfr1ZCaQpFZCCyyoToRhpfyofyoCQAZCENA1grnKauuM1aleFYsDDnmC9Pqw0Y5grHF1QskTmQ07ffkzspV9tdOg3Gm1aBjzS390ss7nVjFOfdE38R7GmyqDh0azfGZCwiuQ8eflLvxZCipMm94yVHQPy408BAQpXeQNjSH32Kf2n8IhDaKQkGOZBeTTwmVEabZB7DQQUGHs1QW8ZD",
    ):
        self.access_token = access_token
        self.server = None

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

    def authenticate_facebook(self):
        # Inicia el servidor temporal en un hilo
        server_thread = threading.Thread(target=self.iniciar_servidor)
        server_thread.start()

        PORT = 8080
        #ID de tu aplicación de Facebook
        APP_ID = '726809776152575'
        # Construye la URL de inicio de sesión de Facebook
        auth_url = f'https://www.facebook.com/v10.0/dialog/oauth?client_id={APP_ID}&redirect_uri=http://localhost:{PORT}/&scope=email,user_posts,user_posts'

        # Abre una ventana del navegador para que el usuario inicie sesión en Facebook
        webbrowser.open(auth_url)

    
    def iniciar_servidor():
        # Puerto para el servidor temporal
        PORT = 8080
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
