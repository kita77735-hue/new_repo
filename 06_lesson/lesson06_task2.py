from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH,
         "//label[text()='Set New Button Name']/following-sibling::input")
    )
)
input_field.send_keys("SkyPro")

button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.btn-primary")
    )
)
button.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "button.btn-primary"),
        "SkyPro"
    )
)

final_text = driver.find_element(By.CSS_SELECTOR, "button.btn-primary").text
print(final_text)

driver.quit()
