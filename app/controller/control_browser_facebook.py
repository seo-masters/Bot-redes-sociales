from controller.selenium_app import Automate
from models.openai_api import OpenAIClient
import re
import pyautogui
from selenium.webdriver.common.by import By
from models.pixabay_api import PixabayAPI
class Control_facebook:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.nave = Automate()

    def facebook_main(self):
        self.nave.open_browser("https://es-la.facebook.com/login/")
        self.login()
        ia = OpenAIClient()
        image = PixabayAPI()
        mensaje = ia.chatGpt(
            "Dame un mensaje para postear en mi facebook- contexto: soy una mujer joven - por favor no incluyas emojis"
        )
        mensaje = re.sub(
            r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001FC00-\U0001FCFF\U0001FD00-\U0001FDFF\U0001FE00-\U0001FEFF\U0001FF00-\U0001FFFF\U00002000-\U0000206F\U00002100-\U000027BF\U00002B05\U00002B06\U00002B07\U00002B1B\U00002B50\U00002B06\U000023E9\U000023F0\U00002B05\U0001F004\U0001F0CF\U00002B05\U00002B06\U00002B07\U00002B1B\U00002B50\U00002B06\U000023E9\U000023F0\U00002B05\U0001F004\U0001F0CF]+",
            "",
            mensaje,
        )
        #url_image = image.get_images("motivate")
        self.publish_post(mensaje)

        self.nave.time_sleep(10)

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
        #self.nave.click_css("[aria-label='Publicar']")
        #pyautogui.press("enter")

