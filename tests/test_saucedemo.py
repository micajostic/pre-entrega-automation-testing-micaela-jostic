"""Casos de prueba automatizados para saucedemo.com."""

import pytest

from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO
from utils import helpers


@pytest.mark.smoke
def test_login_exitoso(driver):
    """Verifica que un usuario válido puede iniciar sesión."""

    helpers.ir_a_login(driver)

    helpers.iniciar_sesion(driver, USUARIO_VALIDO, PASSWORD_VALIDO)

    helpers.esperar_url_contiene(driver, "/inventory.html")

    assert "/inventory.html" in driver.current_url

    titulo = helpers.esperar_elemento(driver, helpers.TITULO_PRODUCTOS)
    assert titulo.text == "Products"

    assert driver.title == "Swag Labs"
    