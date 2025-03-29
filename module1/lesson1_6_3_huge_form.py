# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html). 
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта. 
# В награду за заполнение формы становится доступен код на скидку. 
# Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение. Теперь эта задача под силу только роботам

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 
# from selenium.webdriver.common.by import By 
# библиотека ничего не делает, можно не использовать и добавить скобки
# Пример было - browser.find_element(By.TAG_NAME, 'input')
# Стало - browser.find_element('tag_name', 'input')

try:
    #browser = webdriver.Chrome() - убрал, теперь использую ChromeDriverManager
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements('tag name', 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element('css selector', "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла