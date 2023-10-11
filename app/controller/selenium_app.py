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
import random
import pyperclip
import re


class Automate:
    def __init__(self, proxy=None, port=None, user=None, password=None):
        self.driver = None
        self.proxy = proxy
        self.port = port
        self.user = user
        self.password = password

    def open_browser(self, url, proxy=False):
        try:
            # Crear un objeto ChromeOptions
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")

            # Si se proporcionan detalles del proxy, configurar el proxy
            if proxy:
                chrome_options.add_argument(
                    f"--proxy-server=http://{self.proxy}:{self.port}"
                )

            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(url)
            self.driver.maximize_window()

            if proxy:
                self.time_sleep(5)
                pyautogui.write(self.user)
                pyautogui.press("tab")  # moverse al campo de la contraseña
                pyautogui.write(self.password)
                pyautogui.press("enter")  # enviar el formulario
            return True
        except Exception as e:
            print(f"Error al abrir el navegador: {str(e)}")
            return False

    def click(self, xpath, timeX=10):
        # Esperar hasta que el elemento esté visible y se pueda hacer clic en él
        element = WebDriverWait(self.driver, timeX).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        print(f"Se clickeo: {xpath}")
        element.click()  # Ya que element es el objeto del elemento, puedes hacer clic directamente en él

    def click_css(self, xpath, timeX=10):
        WebDriverWait(self.driver, timeX).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, xpath))
        )
        element = self.driver.find_element(By.CSS_SELECTOR, xpath)
        print(f"Se clickeo: {xpath}")
        element.click()

    def write_text(self, xpath, text, timeX=10, rapido=False, fast_t=0.1):
        # Esperar hasta que el elemento esté visible
        element = WebDriverWait(self.driver, timeX).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        # Si rapido está activado, escribir el texto de una vez
        if rapido:
            element.send_keys(text)
        else:
            # Escribir el texto con un retraso de 100 milisegundos entre cada carácter
            for c in text:
                if self.contains_non_bmp_chars(c):
                    # Si el texto contiene caracteres fuera del BMP, copiar y pegar el texto
                    pyperclip.copy(c)
                    element.send_keys(Keys.CONTROL, "v")
                else:
                    element.send_keys(c)
                numero_aleatorio = random.random()
                # Convertir el número aleatorio a un número entre 0.001 y 0.9
                numero_aleatorio = numero_aleatorio * fast_t + 0.0001
                time.sleep(numero_aleatorio)
    
    def padre(self, xpath_father, xpath_hijo, texto):
        try:
            # Espera hasta que el elemento <span> con el texto "Empieza a escribir" esté visible
            span_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath_father))
            )

            # Encuentra el <textarea> que está dentro del <div> padre
            textarea_element = span_element.find_element(By.XPATH, xpath_hijo)

            # Escribe texto en el <textarea>
            textarea_element.send_keys(texto)
            
            # Puedes también enviar una tecla 'Enter' si es necesario
            # textarea_element.send_keys(Keys.RETURN)

        except Exception as e:
            print(f"Error: {str(e)}")

    def contains_non_bmp_chars(self, text):
        return bool(re.search(r"[^\x00-\xFFFF]", text))

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
            return True
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
