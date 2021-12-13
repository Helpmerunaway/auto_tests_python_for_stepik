from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    price_button = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    # price_button.click()
    book_button = driver.find_element(By.ID, "book")
    book_button.click()
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
    submit_button = driver.find_element(By.ID, "solve")
    submit_button.click()
finally:
    time.sleep(10)
driver.quit()
