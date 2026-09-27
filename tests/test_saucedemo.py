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


def test_agregar_producto_al_carrito(driver):
    """Verifica que se puede agregar un producto al carrito de compras."""

    # Precondicion: iniciar sesion
    helpers.ir_a_login(driver)
    helpers.iniciar_sesion(driver, USUARIO_VALIDO, PASSWORD_VALIDO)
    helpers.esperar_url_contiene(driver, "/inventory.html")

    # 1. El carrito arranca vacio
    assert helpers.contador_carrito(driver) == 0, "El carrito no estaba vacio al inicio"

    # 2. Agregar el primer producto al carrito
    nombre_agregado = helpers.agregar_primer_producto_al_carrito(driver)
    print(f"\nProducto agregado: {nombre_agregado}")

    # 3. El contador del carrito se incremento
    helpers.esperar_contador_carrito(driver, 1)
    assert helpers.contador_carrito(driver) == 1, "El contador del carrito no se incremento"

    # 4. Navegar al carrito
    helpers.ir_al_carrito(driver)
    assert "/cart.html" in driver.current_url, "No navego a la pagina del carrito"

    # 5. El producto agregado aparece en el carrito
    items = helpers.items_del_carrito(driver)
    assert len(items) == 1, f"Se esperaba 1 producto en el carrito y hay {len(items)}"
    assert nombre_agregado in items[0].text, "El producto del carrito no es el que agregue"