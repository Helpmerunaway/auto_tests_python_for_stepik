from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x_element)
    # print(y)
    input_answer = driver.find_element(By.ID, "answer")
    input_answer.click()
    input_answer.send_keys(y)
    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
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
driver.quit()