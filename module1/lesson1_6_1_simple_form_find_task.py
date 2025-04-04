# Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. 
# Если всё сделано правильно, то вы увидите окно с проверочным кодом. 
# Это число вам нужно ввести в качестве ответа в этой задаче.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    input1 = browser.find_element('tag name', 'input')
    input1.send_keys("Ivan")
    
    input2 = browser.find_element('name', 'last_name')
    input2.send_keys("Petrov")
    
    input3 = browser.find_element('css selector', '.form-control.city')
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element('id', 'country')
    input4.send_keys("Russia")
    
    button = browser.find_element('css selector', 'button.btn')
    button.click()

finally:
    time.sleep(15)
    browser.quit()