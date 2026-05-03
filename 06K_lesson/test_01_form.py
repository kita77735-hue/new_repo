import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()


def test_form_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    form_data = {
        "input[name='first-name']": "Иван",
        "input[name='last-name']": "Петров",
        "input[name='address']": "Ленина, 55-3",
        "input[name='e-mail']": "test@skypro.com",
        "input[name='phone']": "+7985899998787",
        "input[name='city']": "Москва",
        "input[name='country']": "Россия",
        "input[name='job-position']": "QA",
        "input[name='company']": "SkyPro"
    }
    for locator, value in form_data.items():
        field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        field.clear()
        field.send_keys(value)
    submit_btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()
    zip_field = browser.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute("class"), "Zip code должен иметь класс alert-danger"
    form_data = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']

    for locator in form_data:
        field = browser.find_element(By.ID, locator)

        assert "alert-success" in field.get_attribute("class"), f"Поле {locator} должно быть валидным"
