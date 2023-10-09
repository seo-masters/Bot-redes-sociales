import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import controller.extension as vt


class Automate:
    def __init__(self):
        self.driver = None

    def open_browser(
        self, url, proxy_ip=None, proxy_port=None, username=None, password=None
    ):
        try:
            # Crear un objeto ChromeOptions
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")

            # Si se proporcionan detalles del proxy, configurar el proxy
            if proxy_ip and proxy_port:
                chrome_options.add_argument(
                    f"--proxy-server=http://{proxy_ip}:{proxy_port}"
                )

            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(url)
            self.driver.maximize_window()

            # Si se proporcionan credenciales y una ruta de imagen, esperar la autenticación
            if username and password:
                # Espera hasta que el cuadro de diálogo de autenticación aparezca
                # for _ in range(60):  # Espera hasta 60 segundos
                #     if pyautogui.locateOnScreen("aut.png"):
                #         break  # Si encuentra el cuadro de diálogo, sale del bucle
                #     time.sleep(1)  # Espera 1 segundo antes de revisar de nuevo
                self.time_sleep(4)
                # Utilizar pyautogui para ingresar las credenciales
                pyautogui.write(username)
                pyautogui.press("tab")  # moverse al campo de la contraseña
                pyautogui.write(password)
                pyautogui.press("enter")  # enviar el formulario

            return True
        except Exception as e:
            print(f"Error al abrir el navegador: {str(e)}")
            return False

    def click(self, xpath, timeX=10):
        try:
            # Esperar hasta que el elemento esté visible y se pueda hacer clic en él
            element = WebDriverWait(self.driver, timeX).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            print(f"Se clickeo: {xpath}")
            element.click()  # Ya que element es el objeto del elemento, puedes hacer clic directamente en él
        except Exception as e:
            print(f"Error al hacer clic en el elemento: {str(e)}")

    def click_css(self, xpath, timeX=10):
        try:
            WebDriverWait(self.driver, timeX).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, xpath))
            )
            element = self.driver.find_element(By.CSS_SELECTOR, xpath)
            print(f"Se clickeo: {xpath}")
            element.click()
        except Exception as e:
            print(f"Error al hacer clic en el elemento: {str(e)}")

    def write_text(self, xpath, text, timeX=10):
        try:
            # Esperar hasta que el elemento esté visible
            element = WebDriverWait(self.driver, timeX).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            element.clear()  # (Opcional) Limpiar cualquier texto existente en el campo antes de escribir
            element.send_keys(text)
        except Exception as e:
            print(f"Error al escribir en el elemento: {str(e)}")

    def clear_input(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element = self.driver.find_element(By.XPATH, xpath)
            element.clear()
        except Exception as e:
            print(f"Error al limpiar el elemento de entrada: {str(e)}")

    def get_text(self, tag_name):
        try:
            element = self.driver.find_element(By.TAG_NAME, tag_name)
            return element.text
        except Exception as e:
            print(f"Error al obtener el texto del elemento {tag_name}: {str(e)}")
            return ""

    def wait_for_new_window(self, old_window_count):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.number_of_windows_to_be(old_window_count + 1)
            )
        except Exception as e:
            print(f"Error al esperar la nueva ventana: {str(e)}")

    def is_visible(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element.is_displayed()
        except Exception as e:
            print(f"Error al verificar si el elemento es visible: {str(e)}")
            return False

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def time_sleep(self, timeX=1):
        time.sleep(timeX)

    def url_actual(self):
        return self.driver.current_url

    def go_to_url(self, url):
        self.driver.get(url)

    def write_text2(self, selector_type, selector, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((selector_type, selector))
            )
            element = self.driver.find_element(selector_type, selector)
            element.send_keys(text)
        except Exception as e:
            print(f"Error al escribir en el elemento: {str(e)}")
