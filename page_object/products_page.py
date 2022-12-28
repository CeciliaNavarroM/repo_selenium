from selenium.webdriver.common.by import By
import time


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_product_to_cart(self):
        self.driver.find_element(By.XPATH, "(//button[contains(.,'Add to cart')])[1]").click()
