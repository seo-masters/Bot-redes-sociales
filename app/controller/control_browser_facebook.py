from controller.selenium_app import Automate
from models.openai_api import OpenAIClient
import re
import pyautogui
from selenium.webdriver.common.by import By
from models.pixabay_api import PixabayAPI
import random
from tkinter import messagebox


class Control_facebook:
    def __init__(self, data, respuesta_queue):
        self.data = data
        self.respuesta_queue = respuesta_queue
        self.proxy = self.data["proxy"]
        print(self.proxy)
        self.nave = Automate(
            self.proxy["address"],
            self.proxy["port"],
            self.proxy["user"],
            self.proxy["password"],
        )

    def facebook_main(self):
        self.nave.open_browser("https://es-la.facebook.com/login/", True)
        self.login(self.data["usuario_cuenta"], self.data["password"])
        ia = OpenAIClient()
        image = PixabayAPI()
        mensaje_historia = ia.chatGpt(
            "Dame un mensaje para postear en una historia de facebook- contexto: soy una mujer joven - por favor no incluyas emojis - maximo 146 caracteres",
            True,
        )
        mensaje = ia.camila_chatbot(
            f"Dame un mensaje para publicar en mi facebook, basado en mi personalidad",
            self.data["personalidad"],
            True,
        )

        #############################
        # MEZCLADOR DE FUNCIONES
        #############################

        flujos = [self.publish_post(mensaje),self.publicar_historia(mensaje_historia) ]

        # Mezcla aleatoriamente la lista de funciones
        flujos = random.shuffle(flujos)
        for funcion in flujos:
            numero_aleatorio = random.randint(10, 15)
            self.nave.time_sleep(numero_aleatorio)
            funcion()
            numero_aleatorio = random.randint(10, 15)
            self.nave.time_sleep(numero_aleatorio)

        


        return self.data["nombre_de_campana"] + " OK"

        # messagebox.showinfo("Título de la Alerta", "Este es el mensaje de la alerta")

    def login(self, user, password):
        if self.nave.is_visible(
            "/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]"
        ):
            self.nave.click("/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]")

        self.nave.write_text(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input",
            user,
            20,
        )
        self.nave.write_text(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input",
            password,
        )
        self.nave.click(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button"
        )
        self.respuesta_queue.put("Se logueo satisfactoriamente")

    def publish_post(self, text_post, url_image=None):
        """Publica un post en facebook user"""
        url = "https://www.facebook.com/"
        print(self.nave.url_actual())

        if self.nave.url_actual() != url:
            self.nave.go_to_url(url)

        self.nave.click(
            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span"
        )
        self.nave.click(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/p"
        )
        self.nave.write_text(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]",
            text_post,
            fast_t=0.1,
        )
        self.nave.click(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/span/div/div/div[1]/div/div/div[1]"
        )

        self.nave.click(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div"
        )
        self.nave.time_sleep(2)
        pyautogui.write(r"C:\Users\USER\Downloads\photo5.jpg")
        pyautogui.press("enter")
        self.nave.time_sleep(2)
        self.nave.click(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]"
        )
        # self.nave.click_css("[aria-label='Publicar']")
        # pyautogui.press("enter")
        self.nave.time_sleep(15)
        self.respuesta_queue.put("Publico un post")
        return True

    def publicar_historia(self, text_post=None, image_url=None):
        """Publica un historia en facebook user"""
        url = "https://www.facebook.com/"
        print(self.nave.url_actual())
        if self.nave.url_actual() != url:
            self.nave.go_to_url(url)

        self.nave.click(
            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/a",
            20,
        )

        if image_url != None:
            self.nave.click(
                "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]",
                30,
            )
            self.nave.time_sleep(2)
            # Toca recortar la foto formato historia
            pyautogui.write(r"C:\Users\USER\Downloads\photo5.jpg")
            pyautogui.press("enter")
            self.nave.click(
                "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div"
            )
        else:
            num = random.randint(1, 16)
            self.nave.time_sleep(2)
            self.nave.click(
                "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]",
                5,
            )
            self.nave.click(
                f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[3]/div[2]/div[{num}]/div/div/img"
            )
            # maximo 146 caracteres
            # self.nave.write_text("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div[3]/div/div[1]/div/label/div/div/textarea", text_post, rapido=True)
            self.nave.padre(
                "//span[text()='Empieza a escribir']", "./../textarea", text_post
            )
            self.nave.click(
                "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[5]/div[2]/div"
            )
            self.nave.time_sleep(10)
        return True

    def comentar(self):
        pass

    def dar_like(self):
        pass

    def revisar_notificaciones(self):
        """abrir devolver dejar limpio scroll y abrir unas dos"""
        pass

    def responder_chat(self):
        """Pueden ser uno o dos mensajes"""
        pass

    def unirse_grupos(self):
        """Unirme a un grupo palabras claves 1 6 aleatori unirme"""
        pass
