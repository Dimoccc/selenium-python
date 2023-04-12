from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math,os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1 = browser.find_element(By.XPATH , "//input[@name = 'firstname']")
input1.send_keys("Ivan")
input2 = browser.find_element(By.XPATH , "//input[@name = 'lastname']")
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH ,"//input[@name = 'email']")
input3.send_keys("Smolensk")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'txt.txt')           # добавляем к этому пути имя файла 
element =browser.find_element(By.XPATH , "//input[@name = 'file']")
element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()