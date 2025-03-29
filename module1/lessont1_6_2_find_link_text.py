# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

# Добавьте в самый верх своего кода import math
# Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: 
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде) 

# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

# Заполните скриптом форму так же как вы делали в предыдущем шаге урока

# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    browser.find_element('partial link text', text).click()
    

    input1 = browser.find_element('tag name', "input")
    input1.send_keys("Lox")
    input2 = browser.find_element('name', "last_name")
    input2.send_keys("Loxov")
    input3 = browser.find_element('class name', "form-control.city")
    input3.send_keys("Loxovsk")
    input4 = browser.find_element('id', "country")
    input4.send_keys("Russia")
    button = browser.find_element('css selector', "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()