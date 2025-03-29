# Ваша программа должна:

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html" 
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)
    case = browser.find_element('xpath', "//img[@id='treasure']")
    x = case.get_attribute('valuex') 
    #print('**********************', x)
    y = calc(x)
    y_element = browser.find_element('xpath', "//input[@id ='answer']")
    y_element.send_keys(y)
    checkbox = browser.find_element('xpath' ,"//input[@type='checkbox']")
    checkbox.click()
    radiobox = browser.find_element('xpath', "//input[@id = 'robotsRule']")
    radiobox.click()
    button = browser.find_element('css selector', "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()