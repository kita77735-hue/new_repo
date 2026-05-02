from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#зайти на сайт
driver.get("https://www.labirint.ru/")

# найти книги по слову python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python", Keys.ENTER)

# найти все карточки локаторов
book_locator = "//div[contains(translate(@data-name, 'PYTHON', 'python'), 'python')]"
finded_books = driver.find_elements(By.XPATH, book_locator)

print(f" Найдено книг: {len(finded_books)}\n")

# Вывести в консоль: название, автор, цена
for book in finded_books:
    try:
        title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text.strip()
    except:
        title = "Не указано"
    
    try:
        author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text.strip()
    except:
        author = "Не указан"
    
    try:
        price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text.strip()
    except:
        price = "Не указана"
    
    print(f"📚 {title} | ✍️ {author} | 💰 {price}")

sleep(2)
driver.quit()  