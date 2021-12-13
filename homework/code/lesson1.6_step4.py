from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    # driver = webdriver.Chrome(executable_path=r"C:/drivers/chromedriver")  # <- Путь до файла хромдрайвера
    driver.get(link)

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

# не забываем оставить пустую строку в конце файла