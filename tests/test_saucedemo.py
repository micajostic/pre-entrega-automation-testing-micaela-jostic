"""Casos de prueba automatizados para saucedemo.com."""

import pytest

from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO
from utils import helpers


@pytest.mark.smoke
def test_login_exitoso(driver):
    """Verifica que un usuario valido puede iniciar sesion."""

    helpers.ir_a_login(driver)

    helpers.iniciar_sesion(driver, USUARIO_VALIDO, PASSWORD_VALIDO)

    helpers.esperar_url_contiene(driver, "/inventory.html")

    assert "/inventory.html" in driver.current_url

    titulo = helpers.esperar_elemento(driver, helpers.TITULO_PRODUCTOS)
    assert titulo.text == "Products"

    assert driver.title == "Swag Labs"


def test_catalogo_de_productos(driver):
    """Verifica el titulo, los productos visibles y los elementos de interfaz."""

    # Precondicion: iniciar sesion
    helpers.ir_a_login(driver)
    helpers.iniciar_sesion(driver, USUARIO_VALIDO, PASSWORD_VALIDO)
    helpers.esperar_url_contiene(driver, "/inventory.html")

    # 1. El titulo de la pagina es el correcto
    titulo = helpers.esperar_elemento(driver, helpers.TITULO_PRODUCTOS)
    assert titulo.text == "Products", f"El titulo era '{titulo.text}'"

    # 2. Hay productos visibles
    productos = helpers.listar_productos(driver)
    assert len(productos) > 0, "No se encontro ningun producto en el inventario"

    # 3. El primer producto tiene nombre y precio
    nombre, precio = helpers.datos_primer_producto(driver)
    print(f"\nPrimer producto: {nombre} - {precio}")
    assert nombre != "", "El nombre del primer producto esta vacio"
    assert precio.startswith("$"), f"El precio no tiene formato valido: '{precio}'"

    # 4. Los elementos clave de la interfaz estan presentes
    menu = helpers.esperar_elemento(driver, helpers.BOTON_MENU)
    assert menu.is_displayed(), "El boton de menu no esta visible"

    filtro = helpers.esperar_elemento(driver, helpers.FILTRO_ORDEN)
    assert filtro.is_displayed(), "El filtro de orden no esta visible"