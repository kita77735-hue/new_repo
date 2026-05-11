from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def make_screenshot(x):
    x.maximize_window()
    x.get("https://ya.ru")
    x.save_screenshot('.ya_'+x.name+'.png')
    x.quit()  # закрываем браузер сразу после работы

# Запускаем каждый браузер по очереди
chrome = webdriver.Chrome()
make_screenshot(chrome)

ff = webdriver.Firefox()
make_screenshot(ff)

service = EdgeService(executable_path=r"C:\Users\ASUS\Downloads\msedgedriver.exe")
edge = webdriver.Edge(service=service)
make_screenshot(edge)