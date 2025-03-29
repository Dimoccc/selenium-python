# https://tproger.ru/articles/pytest-fikstury-na-chelovecheskom

import pytest
import time

@pytest.mark.usefixtures("get_driver") # Вызываем фикстуру над классом. Маркер (декоратор) для вызова фикстуры
class Test_example:

    def test_generate_date(self, generate_data):
        login = generate_data["login"] # Записываем в переменную сгенерированный логин
        password = generate_data["password"]
        assert login is not None
        print(login,password)

    @pytest.mark.usefixtures("generate_data_second") # Вызываем фикстуру над методов. Маркер (декоратор) для вызова фикстуры
    def test_1(self):
        print(self.login) # Сюда передастся логин
        print(self.password) # А сюда пароль
        assert self.login is not None
    
    def test_get_url(self):
        self.driver.get("https://yandex.ru") # Работаем с полученным обьектом драйвера
        