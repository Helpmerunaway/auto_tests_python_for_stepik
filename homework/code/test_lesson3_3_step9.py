"""
Если нужно проверить что тест вызывает ожидаемое исключение
то можно воспользоваться специальной конструкцией with.pytest.raises()
Можно проверить что на странице сайта не должен отобраться какой либо элемент
"""

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

"""
В первом тесте элемент будет найден, поэтому ошибка, которую
ожидает менеджер не возникнет и тест упадет.
"""

def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


"""
Во втором тесте кнопка не будет найдена и тест пройдет
"""


def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()