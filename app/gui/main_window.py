import tkinter as tk
from api.facebook_api import FacebookAPI
from api.openai_api import OpenAIClient
from api.facebook2 import FacebookAPI2


class MiVentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # ...otros widgets...

        # Botón "Run" para obtener información del perfil de Facebook
        self.run_button = tk.Button(self, text="Run", command=self.ejecutar_facebook_api)
        self.run_button.pack()

        # Botón "OpenIA" para realizar alguna otra acción
        self.otro_button = tk.Button(self, text="OpenIA", command=self.ejecutar_openai_api)
        self.otro_button.pack()

        # Botón "Pruebas" para realizar alguna otra acción
        self.otro_button = tk.Button(self, text="Facebook2", command=self.generar_token)
        self.otro_button.pack()

    def ejecutar_openai_api(self):
        openai_client = OpenAIClient('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')  # Reemplaza con tu clave de API
        input_message = "dame una palabra de amor en español"
        generated_text = openai_client.generar_texto(input_message)
        print(generated_text)


    def ejecutar_facebook_api(self):
        # Ejecutar publicacion
        #obtenerData()
        access_token = 'EAAKVB5aG3ZC8BO1gTpc7bnqb8MsZAE0zv0MGZAZCZC03lxdg7UpffyfCQQl5NyKXIoEvzDSnRHZCaraQAijNxLarYQkbfZAw47YbLUhVXZB8EaFZBnWNZCuYCVhftaZBkSOUJwjc3T4g5ZAA17S6o3NADCx9kNonWlZC7HozK6Ish8LvIogCYTXzI4zcOcUkeCPU1XefocWZAWs98dmK0t8i1jrA4rp0uMFW45xQgZD'

        # Crea una instancia de la clase FacebookAPI
        facebook_api = FacebookAPI(access_token)

        # Mensaje que deseas publicar
        message = "Hola mundo api Python 6pm"

        # Realiza la publicación en el muro
        success, message = facebook_api.publicar_en_muro(message)
        if success:
            print(message)
        else:
            print(message)

    def generar_token(self):
        facebook_3 = FacebookAPI2("149414758247584","0d235772323370d051639fab3b59bbd5","EAAKVB5aG3ZC8BO23zrQFjix4cIDDMj1fgRqmuOBlQmRnuYlph6STjHAI9xuonIczsixnl8jj8WdNwxbC7K0eArpSZBxlSpz3jnBQsDgSmK9ZCQxsAAazdpInHCUiQYhJjBi9GYuiOXFjtia4IASHpWHWMgk2GXNTSV5XQkXJLZAZCBxacbZAuILavrqt3XgBN2rwYUzaBmfJZBPAB3ZAAhMSfZBcXEwZDZD")
        facebook_3.publicar_en_muro("publicar_en_muro")
        

# Ejemplo de cómo se podría ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentanaPrincipal(master=root)
    app.mainloop()