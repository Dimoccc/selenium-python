# Открыть страницу https://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import Select
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

number = browser.find_element('xpath', "//span[@id='input_value']").text
y = calc(int(number))

y_element = browser.find_element('xpath', "//input[@id ='answer']")
y_element.send_keys(y)

checkbox = browser.find_element('xpath' ,"//input[@type='checkbox']")
checkbox.click()

button = browser.find_element('css selector', "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
radiobox = browser.find_element('xpath', "//input[@id = 'robotsRule']")
radiobox.click()

button.click()
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
