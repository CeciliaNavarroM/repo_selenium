import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_comprar_productos():
    # Abrir el sitio web
    driver = webdriver.Chrome()

    # Iniciar sesión
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)

    # Añadir productos al carrito de compra
    driver.find_element(By.XPATH, "(//button[contains(.,'Add to cart')])[1]").click()

    # Verificar que se ha añadido el producto al mini carrito
    items_in_cart = driver.find_elements(By.XPATH, "//a[contains(@class,'shopping_cart_link')]")
    assert len(items_in_cart) == 1, f"Se esperaba un producto en el carrito, pero se encontraron {len(items_in_cart)}"

    # Hacer clic en el mini carrito y seguir al checkout
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    # Ingresar los datos del checkout y generar la compra
    driver.find_element(By.ID, "first-name").send_keys("Prueba")
    driver.find_element(By.ID, "last-name").send_keys("Automatizada")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)

        # Encontrar todos los elementos que contienen el nombre del producto en el carrito
    items_in_cart = driver.find_elements(By.XPATH, "(//div[contains(@class,'cart_quantity')])[2]")

    # Verificar que solo hay un producto en el carrito
    assert len(items_in_cart) == 1, f"Se encontraron {len(items_in_cart)} productos en el carrito, se esperaba 1"

   
    # Cerrar el navegador
    driver.close()
