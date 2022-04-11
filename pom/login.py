from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
"""
    Функции для проверки формы входа в личный кабинет,
    используются в test_site.py
"""


class Login(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__login_page: str = '/html/body/header/div[2]/nav/div/a[1]'
        self.__login_page_title: str = '//*[@id="app"]/div[1]/div/h1'
        self.__login_field: str = '//*[@id="app"]/div[1]/div/form/div[1]/input'
        self.__password_field: str = '//*[@id="app"]/div[1]/div/form/div[2]/input'
        self.__submit_button: str = '//*[@id="app"]/div[1]/div/form/div[3]/button'
        self.__login_failed: str = '//*[@id="app"]/div[1]/div/form/div[1]'

    def get_login_page(self) -> WebElement:
        return self.is_visible('xpath', self.__login_page, 'Login_page')

    def get_login_page_title(self) -> WebElement:
        return self.is_visible('xpath', self.__login_page_title, 'Login_page_title')

    def get_login_page_title_text(self) -> str:
        title = self.get_login_page_title()
        title_text = title.get_attribute('innerText')
        return title_text

    def get_login_field(self) -> WebElement:
        return self.is_visible('xpath', self.__login_field, 'Login_field')

    def get_password_field(self) -> WebElement:
        return self.is_visible('xpath', self.__password_field, 'Password_field')

    def get_submit_button(self) -> WebElement:
        return self.is_visible('xpath', self.__submit_button, 'Submit_button')