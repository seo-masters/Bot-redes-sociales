import tkinter as tk
from ttkthemes import ThemedTk
# from gui.main_window import MiVentanaPrincipal
from gui.main_view import MiVentanaPrincipal

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Redes Sociales")
        self.root.geometry("400x300")
        self.ventana_principal = MiVentanaPrincipal(root)
        self.ventana_principal.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = ThemedTk(theme="radiance")
    app = MiAplicacion(root)
    root.mainloop()
