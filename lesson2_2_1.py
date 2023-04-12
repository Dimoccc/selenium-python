from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html" # Убери решетку, получишь 2 результат)
    browser = webdriver.Chrome()
    browser.get(link)

    number = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    number2 = browser.find_element(By.XPATH, "//span[@id='num2']").text
    sum = int(number) + int(number2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum)) # ищем элемент sum

    print('*************',number,number2,sum)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()