
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
    
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
    
    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
    
    def enter_zip_code(self, zip_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def click_submit(self):
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
