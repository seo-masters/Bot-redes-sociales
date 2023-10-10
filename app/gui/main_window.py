import tkinter as tk
from controller.main import Controller
import threading
import queue

class MiVentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.controlador = Controller()
        self.create_widgets()


    def create_widgets(self):
        # Widgets.

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="Token Facebook", command=self.btn_token_facebook,
        )
        self.run_button.pack()

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="Publicar en Pagina de Facebook foto url", command=self.btn_publicar_post,
        )
        self.run_button.pack()

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="Selenium", command=self.btn_selenium
        )
        self.run_button.pack()

        #Btn Publicar post en pagina de facebook
        self.run_button = tk.Button(
            self, text="GPT", command=self.btn_chat_gpt
        )
        self.run_button.pack()

        #Btn ejecutar bot
        self.btn_run_bot1 = tk.Button(
            self, text="RUN BOT", command=self.btn_run_bot
        )
        self.btn_run_bot1.pack()

        # Caja de texto para el input
        self.text_entry = tk.Entry()
        self.text_entry.pack()

        # Etiqueta para mostrar más información sobre el botón 0
        self.info_label = tk.Label(
            self, text="Información adicional"
        )
        self.info_label.pack(side=tk.BOTTOM)

        
    def btn_publicar_post(self):
        """llama al controlador Publica una imagen en una página de Facebook."""
        rta = self.controlador.post_to_facebook_page_url()
        self.info_label['text'] = f"Rta: {rta}"
    
    def btn_token_facebook(self):
        print("hola mundo")
        rta = self.controlador.generar_token_facebook()
        self.info_label['text'] = f"Rta: {rta}"

    def btn_selenium(self):
        rta = self.controlador.madurar_perfil()
        self.info_label['text'] = f"Rta: {rta}"

    def btn_chat_gpt(self):
        rta = self.controlador.chat_gpt(self.text_entry.get())
        print(rta)
        self.info_label['text'] = f"Rta: {rta}"

    def btn_run_bot(self):
        self.btn_run_bot1['text'] = "Ejecutando..."
        # Crear una cola para pasar la respuesta desde el hilo de bot
        respuesta_queue = queue.Queue()

        # Crear un hilo para ejecutar la función
        bot_thread = threading.Thread(target=lambda: self.run_bot(respuesta_queue))

        # Iniciar el hilo
        bot_thread.start()


    def run_bot(self, respuesta_queue):
        # Ejecutar la función en un hilo separado
        rta = self.controlador.madurar_perfil(respuesta_queue)
        
        # Poner el resultado en la cola
        respuesta_queue.put(rta)

        # Hacer algo con la respuesta, por ejemplo, mostrarla en la interfaz de usuario
        self.btn_run_bot1['text'] = "RUN"
        respuesta = respuesta_queue.get()
        self.info_label['text'] = f"{respuesta}"
    



# Ejemplo de cómo se podría ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentanaPrincipal(master=root)
    app.mainloop()
