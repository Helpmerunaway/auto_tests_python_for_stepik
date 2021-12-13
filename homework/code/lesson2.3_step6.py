from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    enter_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    enter_button.click()
    # заводим переменную для текущего окна
    first_window = driver.window_handles[0]
    # заводим переменную для второго окна
    new_window = driver.window_handles[1]
    # меняем вкладку на второе окно, активно может быть только одно
    driver.switch_to.window(new_window)

    # функция вычисления логарифма из задачи
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # находим элемент икса на странице
    x_element = driver.find_element(By.ID, "input_value")
    # переводим элемент в текстовой формат
    x = x_element.text
    # получаем результат вычислений подставив x в качестве переменной в функцию calc
    result = calc(x)
    input_answer = driver.find_element(By.ID, "answer")
    input_answer.click()
    input_answer.send_keys(result)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
finally:
    time.sleep(10)
driver.quit()