from selenium.webdriver.common.by import By

class MiniCartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_mini_cart(self):
        # Encontrar y hacer clic en el botón "MINI CART"
        mini_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        mini_cart_button.click()
    def clic_checkout(self):
        check_button = self.driver.find_element(By.ID, "checkout")
        check_button.click()

    def remove_product(self): 
        remove_button = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_button.click()


    def get_product_count(self):
        # Encontrar el elemento que muestra la cantidad de productos en el mini carrito
 
        product_count_element = self.driver.find_element(By.XPATH, "//a[contains(@class,'shopping_cart_link')]")
        # Obtener el valor del elemento y convertirlo a entero
        return int(product_count_element.text)
