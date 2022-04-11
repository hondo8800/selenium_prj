from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
"""
    Функции для проверки шрифтов на главной странице,
    используются в test_site.py
"""


class MainPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__right_title: str = "//button/span[text()='Найти']"

    def get_right_title(self) -> WebElement:
        return self.is_visible('xpath', self.__right_title, 'right_title')

    def get_right_title_text(self) -> str:
        title = self.get_right_title()
        title_text = title.value_of_css_property("font-family")
        return title_text
