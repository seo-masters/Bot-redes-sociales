import tkinter as tk
from tkinter import ttk  # Importando ttk
from controller.main import Controller
import threading
import queue

class MiVentanaPrincipal(ttk.Frame):  # Cambiado tk.Frame a ttk.Frame
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)  # Modificado para expandir el frame
        self.controlador = Controller()
        self.create_widgets()

    def create_widgets(self):
        self.info_label = ttk.Label(self, text="Información")
        self.info_label.pack(side=tk.TOP, fill=tk.X)

        self.text_entry = ttk.Entry(self)
        self.text_entry.pack(fill=tk.X, padx=5, pady=5)

        self.btn_run_bot1 = ttk.Button(self, text="RUN BOT", command=self.btn_run_bot)  # Cambiado tk.Button a ttk.Button
        self.btn_run_bot1.pack(side=tk.BOTTOM, anchor=tk.SE)

    def btn_run_bot(self):
        self.btn_run_bot1["text"] = "Ejecutando..."
        # Crear una cola para pasar la respuesta desde el hilo de bot
        respuesta_queue = queue.Queue()

        # Crear un hilo para ejecutar la función
        bot_thread = threading.Thread(
            target=lambda: self.ejecutar_proceso(respuesta_queue)
        )

        # Iniciar el hilo
        bot_thread.start()

    def ejecutar_proceso(self, respuesta_queue):
        # Ejecutar la función en un hilo separado
        rta = self.controlador.madurar_perfil(respuesta_queue)

        # Poner el resultado en la cola
        respuesta_queue.put(rta)

        # Hacer algo con la respuesta, por ejemplo, mostrarla en la interfaz de usuario
        self.btn_run_bot1["text"] = "RUN"
        respuesta = respuesta_queue.get()
        self.info_label["text"] = f"{respuesta}"

