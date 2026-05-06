from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name = (By.CSS_SELECTOR, "#first-name")
        self.last_name = (By.CSS_SELECTOR, "#last-name")
        self.postal_code = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.total_label = (By.CSS_SELECTOR, "[data-test='total-label']")

    def fill_customer_info(self, first, last, postal):
        self.wait.until(
            EC.presence_of_element_located(self.first_name)
        ).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)

    def continue_checkout(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        )
        element.click()

    def get_total_price(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.total_label)
        )
        return element.text
