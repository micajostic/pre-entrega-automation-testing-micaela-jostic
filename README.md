# Pre-entrega — Automatización de Pruebas con Selenium

Automatización de los flujos principales de [saucedemo.com](https://www.saucedemo.com)
utilizando Selenium WebDriver y Pytest.

Proyecto realizado como pre-entrega del curso de **QA Automation** — Agencia de
Habilidades para el Futuro, Ciudad de Buenos Aires.

---

## Propósito

Validar de forma automatizada los flujos críticos de la aplicación demo
saucedemo.com, verificando que un usuario pueda autenticarse correctamente,
navegar por el catálogo de productos y agregar artículos al carrito de compras.

El proyecto aplica buenas prácticas de automatización: separación de datos y
lógica, esperas explícitas, tests independientes entre sí y un repositorio
centralizado de selectores.

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3.13** | Lenguaje principal |
| **Pytest** | Framework de testing y fixtures |
| **Selenium WebDriver** | Automatización del navegador |
| **pytest-html** | Generación de reportes en HTML |
| **Git / GitHub** | Control de versiones |

---

## Estructura del proyecto

```
pre-entrega-automation-testing-micaela-jostic/
│
├── tests/
│   └── test_saucedemo.py    Casos de prueba
│
├── utils/
│   ├── config.py            URLs, credenciales y tiempos de espera
│   └── helpers.py           Selectores y funciones auxiliares
│
├── reports/                 Reportes HTML generados
│
├── conftest.py              Fixture del navegador (setup / teardown)
├── pytest.ini               Configuración de Pytest y markers
├── requirements.txt         Dependencias del proyecto
└── README.md
```

La separación entre `tests/` y `utils/` es deliberada: los casos de prueba
describen **qué** se valida, mientras que las funciones auxiliares encapsulan
**cómo** se interactúa con la página. Si el sitio cambia un selector, el ajuste
se hace en un único lugar.

---

## Instalación

Requisitos previos: **Python 3.10 o superior** y **Google Chrome** instalado.

```bash
git clone https://github.com/TU-USUARIO/pre-entrega-automation-testing-micaela-jostic.git
cd pre-entrega-automation-testing-micaela-jostic
pip install -r requirements.txt
```

> Selenium 4 gestiona automáticamente el ChromeDriver, por lo que no es
> necesario descargarlo ni configurarlo manualmente.

---

## Ejecución de las pruebas

Ejecutar todas las pruebas:

```bash
pytest -v
```

Ejecutar únicamente las pruebas críticas:

```bash
pytest -v -m smoke
```

Generar el reporte HTML:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

El reporte queda disponible en `reports/reporte.html` y puede abrirse
directamente en el navegador.

---

## Casos de prueba

| Test | Marker | Qué valida |
|---|---|---|
| `test_login_exitoso` | `smoke` | Login con credenciales válidas, redirección a `/inventory.html` y presencia del título "Products" |

---

## Credenciales de prueba

El sitio saucedemo.com es un entorno público de práctica. Las credenciales
utilizadas son las que la propia aplicación publica en su pantalla de login:

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

---

## Autora

**Micaela Jostic** — Curso de QA Automation
