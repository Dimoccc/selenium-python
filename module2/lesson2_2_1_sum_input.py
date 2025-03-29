# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html" 
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    number = browser.find_element('xpath', "//span[@id='num1']").text
    number2 = browser.find_element('xpath', "//span[@id='num2']").text
    sum = int(number) + int(number2)
    
    select = Select(browser.find_element('tag name', "select"))
    select.select_by_value(str(sum)) # ищем элемент sum

    print('*************',number,number2,sum)
    button = browser.find_element('css selector', "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()