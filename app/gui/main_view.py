import tkinter as tk
from tkinter import ttk
from threading import Thread
import queue
from tkinter.scrolledtext import ScrolledText
from controller.main import Controller
from controller.facebook_controller import Controller_facebook

class MiVentanaPrincipal(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.controlador = Controller()
        self.Controller_facebook = Controller_facebook()
        self.create_widgets()
        self.proceso_queue = queue.Queue()  # Cola para procesos

    def create_widgets(self):
        self.info_label = ttk.Label(self, text="Información")
        self.info_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Crear ScrolledText widget
        self.scroll_text_info = ScrolledText(self, wrap=tk.WORD, width=40, height=10)
        self.scroll_text_info.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.btn_run_bot1 = ttk.Button(self, text="RUN BOT", command=self.btn_run_bot)
        self.btn_run_bot1.pack(side=tk.BOTTOM, anchor=tk.CENTER, padx=5, pady=5)

    def btn_run_bot(self):
        self.btn_run_bot1["text"] = "Ejecutando..."
        proceso_thread = Thread(target=self.ejecutar_proceso)
        proceso_thread.start()
        self.master.after(100, self.check_queue)  # Checar la cola cada 100 ms

    def ejecutar_proceso(self):
        self.Controller_facebook.madurar_perfil(self.proceso_queue)

    def check_queue(self):
        try:
            resultado = self.proceso_queue.get(0)
            # Concatenar el mensaje nuevo al final del scroll_text
            self.scroll_text_info.insert("end", f"-> {resultado} \n")

            # Desplazar el scroll_text hasta que el mensaje nuevo esté visible
            self.scroll_text_info.see("end")

            self.btn_run_bot1["text"] = "RUN BOT"
        except queue.Empty:
            self.master.after(100, self.check_queue)  # Si la cola está vacía, chequear de nuevo



