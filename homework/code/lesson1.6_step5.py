from selenium import webdriver

import time
import math
from selenium.webdriver.common.by import By

a = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(a)
driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path="C:/drivers/chromedriver.exe")  # <- Путь до файла хромдрайвера
try:
    link = "http://suninjuly.github.io/find_link_text"
    driver.get(link)
    button_num = driver.find_element(By.PARTIAL_LINK_TEXT, "224592")
    button_num.click()
    input1 = driver.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()