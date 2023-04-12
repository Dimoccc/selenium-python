from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html" # Убери решетку, получишь 2 результат)
    browser = webdriver.Chrome()
    browser.get(link)
    case = browser.find_element(By.XPATH, "//img[@id='treasure']")
    x = case.get_attribute('valuex') 
    #print('**********************', x)
    y = calc(x)
    y_element = browser.find_element(By.XPATH, "//input[@id ='answer']")
    y_element.send_keys(y)
    checkbox = browser.find_element(By.XPATH ,"//input[@type='checkbox']")
    checkbox.click()
    radiobox = browser.find_element(By.XPATH, "//input[@id = 'robotsRule']")
    radiobox.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()