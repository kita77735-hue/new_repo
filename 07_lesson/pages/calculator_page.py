from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "=": (By.XPATH, "//span[text()='=']"),
        }

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        element = self.wait.until(
            EC.presence_of_element_located(self.delay_input)
        )
        element.clear()
        element.send_keys(str(seconds))

    def click_button(self, label):
        locator = self.buttons[label]
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_result_text(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text
