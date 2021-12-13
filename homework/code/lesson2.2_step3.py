from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    # link1 = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"
    driver = webdriver.Chrome()
    driver.get(link2)

    # Находим число a и число b и переводим в текст
    a = driver.find_element(By.ID, "num1").text
    b = driver.find_element(By.ID, "num2").text
    # Складываем значения цифр num1 и num2 и переводим в строки
    result = str(int(a) + int(b))
    # Используя класс select инициализируем новый объект и передаем ему сумму сложения
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_value(result)
    # Находим кнопку по атрибуту и кликаем по нему
    button_submit = driver.find_element(By.TAG_NAME, "button")
    button_submit.click()
finally:
    # Успеваем скопировать код за 10 секунд
    time.sleep(30)
# Закрываем браузер после всех манипуляций
#driver.quit()
