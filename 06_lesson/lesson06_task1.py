from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ajaxButton"))
)
button.click()

result = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".alert-success"),
        "Data loaded with AJAX get request."
    )
)

message = driver.find_element(By.CSS_SELECTOR, ".alert-success")
print(message.text)

driver.quit()
