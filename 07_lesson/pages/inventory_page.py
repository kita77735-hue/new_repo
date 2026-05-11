from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.add_buttons = {
            "backpack": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"),
            "t-shirt": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"),
        }

    def add_to_cart(self, item_key):
        locator = self.add_buttons[item_key]
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def go_to_cart(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        )
        element.click()
