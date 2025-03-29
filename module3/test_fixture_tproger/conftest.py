# https://tproger.ru/articles/pytest-fikstury-na-chelovecheskom

import pytest
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

@pytest.fixture
def generate_data():
    login = f"autotest_{time.time()}@hyper.org" # Генерирует логин
    password = "512" # Назначает пароль
    return {"login":login, "password": password} # Возвращает логин и пароль

@pytest.fixture
# request — создать
# cls — внутри класса
# имя_переменной — атрибут класса
# создать.внутри_класса.имя_переменной = request.cls.login
def generate_data_second(request):
    request.cls.login = f"autotest_{time.time()}@hyper.org" # Генерирует логин
    request.cls.password = "512" # Назначает пароль

@pytest.fixture
def get_driver(request):
    driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver

