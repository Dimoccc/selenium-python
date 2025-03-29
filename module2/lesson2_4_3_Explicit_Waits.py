
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button2.click()

button3 = browser.find_element(By.XPATH, "//button[@id = 'solve']") 
browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
number = browser.find_element(By.XPATH, "//span[@id='input_value']").text
y = calc(int(number))

y_element = browser.find_element(By.XPATH, "//input[@id ='answer']")
y_element.send_keys(y)

time.sleep(10)

button3.click()



# assert "successful" in message.text