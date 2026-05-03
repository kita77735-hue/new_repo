from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://ya.ru")

# txt = driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="USD"]').text
# print(txt)

# tag = driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="USD"]').tag_name
# print(tag)

# id = driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="USD"]').id
# print(id)

# href = driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="USD"]').get_attribute("href")
# print(href)

# ff = driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="USD"]').value_of_css_property("font-family")
# print(ff)

# color = driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="USD"]').value_of_css_property("color")
# print(color)



# driver.get("http://uitestingplayground.com/visibility")
# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)

# driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
# sleep(1)

# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)


# driver.get("https://demoqa.com/radio-button")
# enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
# print(enabled)

# noRadio_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
# print(noRadio_enabled)

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# cb = driver.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
# print(cb.is_selected())

# cb.click()
# print(cb.is_selected())

driver.get("https://the-internet.herokuapp.com/checkboxes")
# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# a = div.find_element(By.CSS_SELECTOR, "a")
# print(a.get_attribute("href"))

divs = driver.find_elements(By.CSS_SELECTOR, 'div')
# l = len(divs)
# print(l)

div = divs[6]
css_class = div.get_attribute("class")
print(css_class)


sleep(1)
driver.quit()