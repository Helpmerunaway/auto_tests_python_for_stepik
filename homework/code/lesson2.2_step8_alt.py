import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)
    name_input = driver.find_element(By.NAME, "firstname")
    name_input.click()
    name_input.send_keys("Vladimir")
    lastname_input = driver.find_element(By.NAME, "lastname")
    lastname_input.click()
    lastname_input.send_keys("Pukin")
    email_input = driver.find_element(By.NAME, "email")
    email_input.click()
    email_input.send_keys("v.pukin@mail.ru")
    file_path = os.path.join("G:\HOMEWORK\selenium_homework\code\stepic/file.txt")
    file_text = driver.find_element(By.ID, "file")
    file_text.send_keys(file_path)
    button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()
finally:
    time.sleep(5)
driver.quit()