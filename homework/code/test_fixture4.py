import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Запустим все наши тесты из класса TestMainPage1
в одном браузере для экономии времени, задав scope="class" в фикстуре browser:
"""
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

"""
Мы видим, что в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере. 
Здесь мы проделали это в качестве примера, но мы крайне рекомендуем всё же запускать отдельный экземпляр браузера 
для каждого теста, чтобы повысить стабильность тестов. 
Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это работа с базами данных), 
можно вызывать и один раз за сессию запуска тестов.
"""