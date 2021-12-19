from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest


class TestUnit(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver = webdriver.Chrome()
        driver.get(link)
        input_first_name = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group first_class')]//input[contains(@placeholder, 'Input your first name')]")
        input_first_name.click()
        input_first_name.send_keys("Alexey")
        input_second_name = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group second_class')]//input[contains(@placeholder, 'Input your last name')]")
        input_second_name.click()
        input_second_name.send_keys("Nazalny")
        input_email = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group third_class')]//input[contains(@placeholder, 'Input your email')]")
        input_email.click()
        input_email.send_keys("nazanly@mail.ru")
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt, "Успешно")
        time.sleep(10)
        driver.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        driver.get(link)
        input_first_name = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group first_class')]//input[contains(@placeholder, 'Input your name')]")
        input_first_name.click()
        input_first_name.send_keys("Alexey")
        input_phone = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group second_class')]//input[contains(@placeholder, 'Input your phone')]")
        input_phone.click()
        input_phone.send_keys("88005553535")
        input_email = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group third_class')]//input[contains(@placeholder, 'Input your email')]")
        input_email.click()
        input_email.send_keys("nazanly@mail.ru")
        input_address = driver.find_element(By.XPATH, "//div[contains(@class, 'form-group second_class')]//input[contains(@placeholder, 'Input your address')]")
        input_address.click()
        input_address.send_keys("Moscow")
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt, "Успешно")
        driver.quit()

if __name__ == "__main__":
    unittest.main()