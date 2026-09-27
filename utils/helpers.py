"""Funciones auxiliares y selectores del sitio saucedemo.com."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import URL_BASE, TIMEOUT

CAMPO_USUARIO = (By.ID, "user-name")
CAMPO_PASSWORD = (By.ID, "password")
BOTON_LOGIN = (By.ID, "login-button")
TITULO_PRODUCTOS = (By.CLASS_NAME, "title")
MENSAJE_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

def ir_a_login(driver):
    """Abre la pagina de login de saucedemo."""
    driver.get(URL_BASE)

def iniciar_sesion(driver, usuario, password):
    """Completa el formulario de login y hace clic en Login."""
    driver.find_element(*CAMPO_USUARIO).send_keys(usuario)
    driver.find_element(*CAMPO_PASSWORD).send_keys(password)
    driver.find_element(*BOTON_LOGIN).click()

def esperar_url_contiene(driver, texto, timeout=TIMEOUT):
    """Espera explícita: frena hasta que la URL contenga el texto."""
    WebDriverWait(driver, timeout).until(EC.url_contains(texto))

def esperar_elemento(driver, localizador, timeout=TIMEOUT):
    """Espera explícita: frena hasta que el elemento sea visible y lo devuelve."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(localizador)
    )
