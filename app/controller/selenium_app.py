import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Automate:
    def __init__(self):
        self.driver = None

    def open_browser(self, url):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(url)
            
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"Error al abrir el navegador: {str(e)}")
            return False


    def click(self, xpath, timeX=10):
        try:
            WebDriverWait(self.driver, timeX).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element = self.driver.find_element(By.XPATH, xpath)
            print(f"Se clickeo: {xpath}")
            element.click()
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

    def write_text(self, xpath, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element = self.driver.find_element(By.XPATH, xpath)
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


