import time

import pytest

from pom.homepage_nav import HomepageNav, TitleName


@pytest.mark.usefixtures('setup')
class TestHomepage:

    """def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
        elements = homepage_nav.get_nav_links()
        for element in elements:
            element.click()
        time.sleep(3)"""

    def test_title_name(self):
        title = TitleName(self.driver)
        #print(title.get_title_text())
        title.get_title().click()
        time.sleep(3)

        login = TitleName(self.driver)
        #print(login.get_login_page_text())
        expected_title = 'Вход в личный кабинет'
        actual_title = login.get_login_page_text()
        assert expected_title == actual_title, 'Switch page to "account"'
        time.sleep(3)


