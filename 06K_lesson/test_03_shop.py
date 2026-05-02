import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


def test_shop_checkout(browser):
    browser.get("https://www.saucedemo.com/")
    wait = WebDriverWait(browser, 10)
    username_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
    )
    username_field.send_keys("standard_user")
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    password_field.send_keys("secret_sauce")
    login_btn = browser.find_element(By.CSS_SELECTOR, "#login-button")
    login_btn.click()
    backpack_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
    )
    backpack_btn.click()
    tshirt_btn = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt_btn.click()
    onesie_btn = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    onesie_btn.click()
    cart_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link"))
    )
    cart_link.click()
    checkout_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
    )
    checkout_btn.click()
    first_name = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name"))
    )
    first_name.send_keys("Никита")
    last_name = browser.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Пономарев")
    postal_code = browser.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("123456")
    continue_btn = browser.find_element(By.CSS_SELECTOR, "#continue")
    continue_btn.click()
    total_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))
    )
    total_price = total_element.text
    assert "$58.29" in total_price or "58.29" in total_price, \
        f"Ожидали $58.29, но получили: {total_price}"
