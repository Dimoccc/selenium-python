import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# вызов pytest -s -v -m "smoke and win10" test_fixture_mark2_win10.py
# -s вывод принт
# -v - режим verbous (многословный). Детально расскажет о прохождении.
#-rx - report on XFAIL (отчитаться о наличии метки XFAIL). 
# В целом, даже без (remark = "") покажет в каком тесте была метка. 
#-m markers
# mark.skip - skip def

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
