from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = driver.find_element(By.ID, "verify_message")

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(driver, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

assert "successful" in message.text