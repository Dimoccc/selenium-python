import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
link = "http://selenium1py.pythonanywhere.com/"
# user_language = "en-GB"  # можно сменить для проверки
# user_language = 'ru-RU'

def test_language(browser):
    # options = Options()
    # options.add_argument("--lang=" + user_language)
    # browser= webdriver.Chrome(options=options)

    browser.get(link)
    time.sleep(3)
    browser.quit()