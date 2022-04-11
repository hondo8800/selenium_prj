import time

import pytest

from pom.login import Login
from pom.main_page import MainPage


@pytest.mark.usefixtures('setup')
class TestSite:

    def test_switch_to_login_page(self):
        """переход на страницу логина"""
        login_page = Login(self.driver)
        login_page.get_login_page().click()
        expected_title = 'Вход в личный кабинет'
        actual_title = login_page.get_login_page_title_text()
        assert expected_title == actual_title, 'Switch page to "account"'

        """ввод логина"""
        login_field = Login(self.driver)
        login_field.get_login_field().send_keys("ostyakovp@gmail.com")

        """ввод пароля"""
        password_field = Login(self.driver)
        password_field.get_password_field().send_keys("7654321")

        """нажатие кнопки Продолжить"""
        submit_button = Login(self.driver)
        submit_button.get_submit_button().click()
        time.sleep(3)

    def test_fonts(self):
        """проверка шрифта"""
        right_title = MainPage(self.driver)
        print(right_title.get_right_title_text())


