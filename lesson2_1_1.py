from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    #link = "http://suninjuly.github.io/registration1.html" # Убери решетку, получишь 1 результат)
    link = "https://suninjuly.github.io/math.html" # Убери решетку, получишь 2 результат)
    browser = webdriver.Chrome()
    browser.get(link)

    #Работает на 2 страницах, не уникальные селекторы
    #elements = browser.find_elements(By.XPATH, "//div[@class='first_block']/child::div/input")
    #for element in elements:
    #     element.send_keys("абоба")
   
    #input1 = browser.find_element(By.XPATH , "//div/label/span[@id= 'input_value']")
    x_element = browser.find_element(By.XPATH , "//div/label/span[@id= 'input_value']")
    x = x_element.text
    y = calc(x)
    y_element=browser.find_element(By.XPATH, "//input[@class ='form-control']")
    y_element.send_keys(y)
    checkbox = browser.find_element(By.XPATH ,"//input[@type='checkbox']")
    checkbox.click()
    radiobox = browser.find_element(By.XPATH, "//input[@id = 'robotsRule']")
    radiobox.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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
