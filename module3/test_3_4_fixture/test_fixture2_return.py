#Фикстуры, возвращающие значение - добавлен в отличии от 1 файла 
# return browser для дальнейшей работы -> browser.get(link)

import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# browser, когда обращаемся к браузер, выводим текст
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return browser 



class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")