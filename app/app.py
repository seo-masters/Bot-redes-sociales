import tkinter as tk
from gui.main_window import MiVentanaPrincipal

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Redes xxxxx")
        self.root.geometry("400x300")
        
        self.ventana_principal = MiVentanaPrincipal(root)
        self.ventana_principal.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiAplicacion(root)
    root.mainloop()