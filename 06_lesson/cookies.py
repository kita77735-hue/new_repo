from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get("http://labirint.ru")
driver.add_cookie(my_cookie)

cookie = driver.get_cookie('begintimed')
print(cookie)

cookies = driver.get_cookies()
# print(cookies)

# driver.delete_all_cookies()

# driver.refresh()

# sleep(10)
driver.quit()