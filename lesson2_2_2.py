from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

number = browser.find_element(By.XPATH, "//span[@id='input_value']").text
y = calc(int(number))

y_element = browser.find_element(By.XPATH, "//input[@id ='answer']")
y_element.send_keys(y)

checkbox = browser.find_element(By.XPATH ,"//input[@type='checkbox']")
checkbox.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
radiobox = browser.find_element(By.XPATH, "//input[@id = 'robotsRule']")
radiobox.click()

button.click()
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
