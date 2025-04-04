from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
   # labels = browser.find_element(By.TAG_NAME, 'label')
    #browser.find_elements_by_tag_name('label') # Список лэйблов над текстовыми полями

   # inputs = browser.find_element(By.TAG_NAME, 'input') # Список текстовых полей
    

    #for i, label in enumerate(labels):          # Если последний символ
    #    if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
    #        inputs[i].send_keys('Обязалово!')   # то в поле ввода печатаем "Обязалово!"

    #elements = browser.find_elements(By.XPATH, "//div[@class='first_block']/child::div/input")
   # for element in elements:
    #    element.send_keys("Мой ответ")
    input1 = browser.find_element('xpath' , "//div[@class='first_block']/child::div/input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element('xpath' , "//div[@class='first_block']/child::div/input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element('xpath' ,"//div[@class='first_block']/child::div/input[@class='form-control third']")
    input3.send_keys("Smolensk")
    # Отправляем заполненную форму
    button = browser.find_element('css_selector', "button.btn")
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
