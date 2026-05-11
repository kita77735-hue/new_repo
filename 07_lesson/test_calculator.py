from selenium import webdriver
from pages.calculator_page import CalculatorPage


def driver():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_calculator_result(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    result = page.get_result_text()
    assert result == "15"
