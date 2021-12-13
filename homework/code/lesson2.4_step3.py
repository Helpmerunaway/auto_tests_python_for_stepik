from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"
driver = webdriver.Chrome()
driver.get(link)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(2)
verify_button = driver.find_element(By.ID, "verify")
verify_button.click()
message = driver.find_element(By.ID, "verify_message")
assert "successful" in message.text
driver.quit()