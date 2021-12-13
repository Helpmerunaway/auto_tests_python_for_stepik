import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)
    # вводим имя в поле firstname
    name_input = driver.find_element(By.NAME, "firstname")
    name_input.click()
    name_input.send_keys("Vladimir")
    # вводим фамилию в поле lastname
    lastname_input = driver.find_element(By.NAME, "lastname")
    lastname_input.click()
    lastname_input.send_keys("Pukin")
    # вводим емейл в поле email
    email_input = driver.find_element(By.NAME, "email")
    email_input.click()
    email_input.send_keys("v.pukin@mail.ru")
    # получаем путь к директории текущего исполняемого скрипта lesson2.2_step8
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "../../../../auto_tests_for_stepic/homework/code/file_example.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    file_text = driver.find_element(By.CSS_SELECTOR, "[type='file']")
    file_text.send_keys(file_path)
    button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()
finally:
    time.sleep(5)
driver.quit()