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
        FacebookAPI(access_tokef)

        

# Ejemplo de cómo se podría ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentanaPrincipal(master=root)
    app.mainloop()