
import time
from selenium.webdriver.common.by import By

import unittest
from selenium import webdriver
from page_object.login_page import LoginPage
from page_object.products_page import ProductsPage
from page_object.mini_cart_page import MiniCartPage
from page_object.checkout_page import CheckoutPage

import time

class TestComprarProductos(unittest.TestCase):
  
  def test_login(driver):
    # Abrir el sitio web y realizar el login
    driver = webdriver.Chrome()

    # Iniciar sesión
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Añadir productos al carrito de compra
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()


    mini_cart_page = MiniCartPage(driver)
    assert mini_cart_page.get_product_count() == 1, "El mini carrito debe tener un producto"


    mini_cart_page = MiniCartPage(driver)
    mini_cart_page.open_mini_cart()
    time.sleep(2)

    mini_cart_page.clic_checkout()
    time.sleep(2)
    # Ingresar los datos del checkout y generar la compra
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("Cecilia")
    checkout_page.enter_last_name("Automatizada")
    checkout_page.enter_zip_code("12345")
    checkout_page.click_submit()





   