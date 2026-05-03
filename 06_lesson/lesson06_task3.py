from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

WebDriverWait(driver, 30).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
)

images = driver.find_elements(By.TAG_NAME, "img")
third_img = images[2]

WebDriverWait(driver, 30).until(
    lambda d: d.find_elements(By.TAG_NAME, "img")[2].get_attribute("src")
)

src_value = third_img.get_attribute("src")
print(src_value)

driver.quit()
