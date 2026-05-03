import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_calculator_delay(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(browser, 60)
    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")
    btn_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']")))
    btn_7.click()
    btn_plus = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))
    btn_plus.click()
    btn_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']")))
    btn_8.click()
    btn_equals = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))
    btn_equals.click()
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"),
        message="Результат '15' не появился за 60 секунд"
    )

    screen = browser.find_element(By.CSS_SELECTOR, ".screen")
    assert screen.text == "15", f"Ожидали '15', но на экране: '{screen.text}'"
