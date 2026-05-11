import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
