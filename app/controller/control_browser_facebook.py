from controller.selenium_app import Automate
from models.openai_api import OpenAIClient
import re
import pyautogui
from selenium.webdriver.common.by import By
from models.pixabay_api import PixabayAPI
import random

class Control_facebook:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.nave = Automate()

    def facebook_main(self):
        #self.nave.open_browser("https://www.cual-es-mi-ip.net/","216.173.76.50","6677","axkdvvan","enhq0qdxswlb")
        self.nave.open_browser("https://es-la.facebook.com/login/")
        self.login()
        ia = OpenAIClient()
        image = PixabayAPI()
        mensaje = ia.chatGpt(
            "Dame un mensaje para postear en mi facebook- contexto: soy una mujer joven - por favor no incluyas emojis",
            True
        )
        #url_image = image.get_images("motivate")
        self.publish_post(mensaje)
        #self.publicar_historia(r"C:\Users\USER\Downloads\photo5.jpg")
        mensaje_historia = ia.chatGpt(
            "Dame un mensaje para postear en una historia de facebook- contexto: soy una mujer joven - por favor no incluyas emojis - maximo 146 caracteres",
            True
        )
        self.nave.time_sleep(3)
        self.publicar_historia(mensaje_historia)

        self.nave.time_sleep(1000)

    def login(self):
        self.nave.write_text(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input",
            self.user,
        )
        self.nave.write_text(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input",
            self.password,
        )
        self.nave.click(
            "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button"
        )

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

        self.nave.click("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]")
        self.nave.click_css("[aria-label='Publicar']")
        pyautogui.press("enter")
        self.nave.time_sleep(5)

    def publicar_historia(self, text_post=None, image_url=None):
        """Publica un historia en facebook user"""
        url = "https://www.facebook.com/"
        print(self.nave.url_actual())
        if self.nave.url_actual() != url:
            self.nave.go_to_url(url)
        
        self.nave.click("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/a",20)

        if image_url != None:
            self.nave.click("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]",30)
            self.nave.time_sleep(2)
            #Toca recortar la foto formato historia
            pyautogui.write(r"C:\Users\USER\Downloads\photo5.jpg")
            pyautogui.press("enter")
            self.nave.click("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div")
        else:
            num = random.randint(1, 16)
            self.nave.click("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]",30)
            self.nave.click(f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[3]/div[2]/div[{num}]/div/div/img")
            #maximo 146 caracteres
            self.nave.write_text("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[1]/div/label/div/div/textarea", text_post)
            self.nave.click("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div")


    
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
