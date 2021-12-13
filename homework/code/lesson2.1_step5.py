from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Находим число по ID и делаем его текстом(строкой)
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # Находим по ID инпут и вводим в него значение которое вернула функция
    input_answer = driver.find_element(By.ID, "answer")
    input_answer.click()
    input_answer.send_keys(y)
    # Находим чек-бокс по ID и кликаем по нем
    input_im_robot = driver.find_element(By.ID, "robotCheckbox")
    input_im_robot.click()
    # Находим радиобаттон по ID и кликаем по нему
    input_robots_rule = driver.find_element(By.ID, "robotsRule")
    input_robots_rule.click()
    # Находим кнопку по атрибуту и кликаем по нему
    button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

finally:
    # Успеваем скопировать код за 10 секунд
    time.sleep(10)
# Закрываем браузер после всех манипуляций
driver.quit()


