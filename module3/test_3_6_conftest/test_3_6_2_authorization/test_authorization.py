import pytest
import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By




@pytest.mark.parametrize('url',[ 
                                  "https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"
                               ])
class TestLogin:
    secret_text = ''
    def test_answer_secret(self,load_config,browser, url): 

        config_data = load_config
        # wait = WebDriverWait(browser, 30, poll_frequency=1)

        browser.get(url)
        browser.implicitly_wait(5)

        # WebDriverWait(browser, 15).until(EC.presence_of_element_located(By.XPATH, "//*[@id= 'ember466']"))
        
        button_login = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id= 'ember466']")))
        button_login.click()

        input_login = browser.find_element(By.XPATH, "//*[@id='id_login_email']")
        input_login.send_keys(str(config_data["login"]))

        input_password = browser.find_element(By.XPATH , "//*[@id='id_login_password']")
        input_password.send_keys(str(config_data["password"]))

        button_loggin2 = browser.find_element(By.XPATH, "//*[@id='login_form']/button")  
        button_loggin2.click()
        time.sleep(1)
    
        try:
            browser.find_element(By.XPATH, "//div[@class='lesson__player']//button[@class = 'again-btn white']").click()
        except:
            print("button - 'again-btn white' NO FOUND")
        try:
            input_answer = browser.find_element(By.XPATH, "//div[@class='lesson__player']//textarea")
            input_answer.clear()
        except:
            print("button - 'again-btn white' NO FOUND")

        input_answer.send_keys(math.log(int(time.time())))

        button_answer = browser.find_element('xpath',"//div[@class='lesson__player']//div//button[@class='submit-submission']")
        button_answer.click()

        text_correct = browser.find_element('xpath',("//p[@class='smart-hints__hint']")).text
        assert text_correct == 'Correct!', f'Ожидали  "Correct!" а получили "{text_correct}"'
        # if text_correct != 'Correct!':
        #     print(text_correct)

        time.sleep(2)
        button_again = browser.find_element('xpath' , "//div[@class='lesson__player']//button[@class = 'again-btn white']")
        button_again.click()
        time.sleep(2)
       
        logof =browser.find_element('xpath', "//*[@class='navbar__profile-toggler st-button_style_none']")
        logof.click()
        logof2 = browser.find_element('xpath' , "//*[@data-qa='menu-item-logout']")
        logof2.click()
        logof3 = browser.find_element('xpath' , "//div[@class='modal-popup__container']//footer//button[1]")
        logof3.click()


        time.sleep(5)


