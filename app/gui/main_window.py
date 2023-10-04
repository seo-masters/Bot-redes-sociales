import tkinter as tk
from controller.main import Controller


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
            self, text="Publicar en Pagina de Facebook foto", command=self.controlador.post_to_facebook_page,
        )
        self.run_button.pack()


# Ejemplo de cómo se podría ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentanaPrincipal(master=root)
    app.mainloop()
