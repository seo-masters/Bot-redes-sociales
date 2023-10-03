import tkinter as tk
from api.facebook_api import FacebookAPI
from api.openai_api import OpenAIClient


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
        self.otro_button = tk.Button(self, text="Facebook2", command=self.ejecutar_openai_api)
        self.otro_button.pack()

    def ejecutar_openai_api(self):
        openai_client = OpenAIClient('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')  # Reemplaza con tu clave de API
        input_message = "dame una palabra de amor en español"
        generated_text = openai_client.generar_texto(input_message)
        print(generated_text)


    def ejecutar_facebook_api(self):
        # Ejecutar publicacion
        #obtenerData()
        access_token = 'EAAKVB5aG3ZC8BO1bBPZAF8wNUZCngE9Hk9eB0jQt87FTECTPYJVDB6wfZC7TlP1ZBQef44g9sPq3MaPyiEdtFXoAX9jsMVP0PGkZArDND3c89MiKM01xQn5hnoYCcPBOSmd1QPMud6ZA7A9ZCBlyLlyUmAFp78gry0T9vTPPi0188ZBSaYwKyjIK4pp70OScXAfnaqNsLVl2v4KmuzJK48i3ibeE7GXSVh5oZD'

        # Crea una instancia de la clase FacebookAPI
        facebook_api = FacebookAPI(access_token)

        # Mensaje que deseas publicar
        message = "Hola mundo api Python"

        # Realiza la publicación en el muro
        success, message = facebook_api.publicar_en_muro(message)
        if success:
            print(message)
        else:
            print(message)

        

# Ejemplo de cómo se podría ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentanaPrincipal(master=root)
    app.mainloop()