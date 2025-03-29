# В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# Запустите ваш код.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    input1 = browser.find_element('xpath', "//input[@name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element('xpath', "//input[@name='last_name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element('xpath', "//input[@class='form-control city']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element('xpath', "//input[@id='country']")
    input4.send_keys("Russia")
    button = browser.find_element('xpath', "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()