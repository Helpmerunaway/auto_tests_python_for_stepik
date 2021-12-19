import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


"""
Задание на параметризацию тестов

1) Использовать маркировку pytest для параметризации и передать список ссылок в качестве параметров
2) Использовать осмысленное сообщение об ошибке в проверке теста, а также настроить нужные ожидания
для стабильной работы тестов.
3) В упавших тестов найти кусочки послания. Тест должен падать если текст в опциональном фидбеке
не совпадает со строкой "Correct!". Собрать кусочки текста в одно предложение и отправить в качестве ответа
4) Убедитесь в правильности локального времени (https://time.is/ru/)
Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. 
"""


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_optional_feedback(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer_input = browser.find_element(By.CSS_SELECTOR, '.textarea')
    answer_input.click()
    answer = math.log(int(time.time() + 0.7))
    answer_input.send_keys(answer)
    send_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    send_button.click()
    feedback = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    correct = str(feedback)
    assert "Correct!" in correct, correct
