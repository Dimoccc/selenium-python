# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

number = browser.find_element(By.XPATH, "//span[@id='input_value']").text
y = calc(int(number))

y_element = browser.find_element(By.XPATH, "//input[@id ='answer']")
y_element.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()