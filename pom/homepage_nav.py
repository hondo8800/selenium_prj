from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils
"""
    Функции для проверки навигационной панели на сайте мэйсис
"""


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINK_TEXT = 'Women,Men,Kids & Baby,Home,Shoes,Handbags & Accessories,Jewelry,Sale'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'HeaderNavigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)


class TitleName(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__title: str = 'body > header > div.hidden.xl\:block.w-full.bg-white.border-b.border-gray-300.h-12 > nav > div > a:nth-child(1)'
        self.__login_page: str = '//*[@id="app"]/div[1]/div/h1'

    def get_title(self) -> WebElement:
        return self.is_visible('css', self.__title, 'Title_name')

    def get_login_page(self) -> WebElement:
        return self.is_visible('xpath', self.__login_page, 'Login_page')

    def get_title_text(self) -> str:
        title = self.get_title()
        title_text = title.text
        return title_text

    def get_login_page_text(self) -> str:
        s_text = self.get_login_page()
        s_text_text = s_text.get_attribute("innerText")
        return s_text_text
