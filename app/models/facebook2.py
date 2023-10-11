import webbrowser
import http.server
import socketserver
import threading
from urllib.parse import urlparse, parse_qs

class FacebookAPI:
    def __init__(self):
        self.server = None
        self.token = None

    def authenticate_facebook(self):
        server_thread = threading.Thread(target=self.start_server)
        server_thread.start()

        PORT = 8080
        APP_ID = '1131611421150208'
        REDIRECT_URI = f'http://localhost:{PORT}/'
        auth_url = f'https://www.facebook.com/v18.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URI}'

        webbrowser.open(auth_url)

    def start_server(self):
        PORT = 8080
        Handler = self.make_handler()
        self.server = socketserver.TCPServer(("", PORT), Handler)
        self.server.serve_forever()

    def make_handler(self):
        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self_):
                nonlocal self
                query = urlparse(self_.path).query
                params = parse_qs(query)
                if 'access_token' in params:
                    self.token = params['access_token'][0]
                    print(f'Token obtained: {self.token}')
                    self.stop_server()  # Llama a stop_server() directamente
                else:
                    print('Failed to obtain token')

        return Handler

    def stop_server(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()

# Ejemplo de uso:
if __name__ == "__main__":
    fb_api = FacebookAPI()
    fb_api.authenticate_facebook()







