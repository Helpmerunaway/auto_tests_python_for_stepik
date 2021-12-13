from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    # Вводим имя
    input_first_name = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group first_class')]//input[contains(@placeholder, 'Input your first name')]")
    input_first_name.click()
    input_first_name.send_keys("Alexey")
    # inp1 = browser.find_element_by_css_selector(".first_block .first")
    # nameInput = browser.find_element(By.CSS_SELECTOR, ".first_class [placeholder='Input your first name']")

    # Вводим фамилию
    input_second_name = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group second_class')]//input[contains(@placeholder, 'Input your last name')]")
    input_second_name.click()
    input_second_name.send_keys("Nazalny")
    # inp2 = browser.find_element_by_css_selector(".first_block .second")
    # lastnameInput = browser.find_element(By.CSS_SELECTOR, ".second_class [placeholder='Input your last name']")

    # Вводим е-мейл

    input_email = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group third_class')]//input[contains(@placeholder, 'Input your email')]")
    input_email.click()
    input_email.send_keys("nazanly@mail.ru")
    # inp3 = browser.find_element_by_css_selector(".form-control.third")
    # emailInput = browser.find_element(By.CSS_SELECTOR, ".third_class [placeholder='Input your email']")


    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()