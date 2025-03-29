
# setup_class выполняется один раз перед запуском всех тестовых методов в классе
# teardown_class выполянется один раз после
# setup_method выполняется перед запуском каждого тестового метода в классе
# teardown_method выполняется каждый раз после
# Про декоратор:

# @classmethod декоратор, использованный для удобства чтения кода. 
# Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу.



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

#Setup and teardown
class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
