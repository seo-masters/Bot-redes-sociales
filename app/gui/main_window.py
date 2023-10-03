import tkinter as tk
from api.facebook_api import FacebookAPI


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

    def ejecutar_facebook_api(self):
        # Ejecutar publicacion
        #obtenerData()
        access_token = 'EAAKVB5aG3ZC8BO1bBPZAF8wNUZCngE9Hk9eB0jQt87FTECTPYJVDB6wfZC7TlP1ZBQef44g9sPq3MaPyiEdtFXoAX9jsMVP0PGkZArDND3c89MiKM01xQn5hnoYCcPBOSmd1QPMud6ZA7A9ZCBlyLlyUmAFp78gry0T9vTPPi0188ZBSaYwKyjIK4pp70OScXAfnaqNsLVl2v4KmuzJK48i3ibeE7GXSVh5oZD'

        # Crea una instancia de la clase FacebookAPI
        facebook_api = FacebookAPI(access_token)

        # Mensaje que deseas publicar
        message = "Este es un mensaje hecho con python3"

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