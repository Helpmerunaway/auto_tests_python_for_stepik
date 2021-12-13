from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    enter_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    enter_button.click()
    confirm = driver.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)
    input_answer = driver.find_element(By.ID, "answer")
    input_answer.click()
    input_answer.send_keys(result)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
finally:
    time.sleep(10)
driver.quit()