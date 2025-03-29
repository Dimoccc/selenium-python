from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

try: 
    #link = "http://suninjuly.github.io/registration1.html" # Убери решетку, получишь 1 результат)
    link = "http://suninjuly.github.io/registration2.html" # Убери решетку, получишь 2 результат)
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    #Работает на 2 страницах, не уникальные селекторы
    #elements = browser.find_elements(By.XPATH, "//div[@class='first_block']/child::div/input")
    #for element in elements:
    #     element.send_keys("абоба")
   
    input1 = browser.find_element('xpath' , "//div[@class='first_block']/child::div/input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element('xpath' , "//div[@class='first_block']/child::div/input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element('xpath' ,"//div[@class='first_block']/child::div/input[@class='form-control third']")
    input3.send_keys("Smolensk")    

    button = browser.find_element('css selector', "button.btn")
    button.click()
   
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element('tag name', "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
