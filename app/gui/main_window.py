import tkinter as tk
from controller.main import Controller
from controller.selenium import Automate


class MiVentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.controlador = Controller()
        self.create_widgets()


    def create_widgets(self):
        # Widgets.

        # Botón "Run" para obtener información del perfil de Facebook
        self.run_button = tk.Button(
            self, text="Publicar post mensaje motivacional", command=self.controlador.ejecutar_facebook_api,
        )
        self.run_button.pack()

        # Botón "Run" para obtener información del perfil de Facebook
        self.run_button = tk.Button(
            self, text="Run pexel", command=self.controlador.get_photo_pexels,
        )
        self.run_button.pack()

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="Token Facebook", command=self.btn_token_facebook,
        )
        self.run_button.pack()

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="Publicar en Pagina de Facebook foto url", command=self.controlador.post_to_facebook_page_url,
        )
        self.run_button.pack()

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="Selenium", command=self.controlador.prueba
        )
        self.run_button.pack()

        # Etiqueta para mostrar más información sobre el botón 0
        self.info_label = tk.Label(
            self, text="Información adicional"
        )
        self.info_label.pack(side=tk.BOTTOM)
    
    def btn_token_facebook(self):
        print("hola mundo")
        rta = self.controlador.generar_token_facebook()
        self.info_label['text'] = f"Rta: {rta}"


# Ejemplo de cómo se podría ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentanaPrincipal(master=root)
    app.mainloop()
