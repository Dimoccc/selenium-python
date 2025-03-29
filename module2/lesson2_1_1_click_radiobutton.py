# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    link = "https://suninjuly.github.io/math.html" 
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    x_element = browser.find_element('xpath' , "//div/label/span[@id= 'input_value']")
    x = x_element.text
    y = calc(x)
    y_element=browser.find_element('xpath', "//input[@class ='form-control']")
    y_element.send_keys(y)
    checkbox = browser.find_element('xpath',"//input[@type='checkbox']")
    checkbox.click()
    radiobox = browser.find_element('xpath', "//input[@id = 'robotsRule']")
    radiobox.click()
    button = browser.find_element('css selector', "button.btn")
    button.click()

      

    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()
   
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
