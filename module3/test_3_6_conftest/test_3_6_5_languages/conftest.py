import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    user_language = 'ru'
    options = Options()
    options.add_argument("--lang=" + user_language)
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language,
    })
    browser= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()