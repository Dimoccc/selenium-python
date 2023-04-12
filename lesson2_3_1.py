from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math,os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
number = browser.find_element(By.XPATH, "//span[@id='input_value']").text
y = calc(int(number))

y_element = browser.find_element(By.XPATH, "//input[@id ='answer']")
y_element.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
