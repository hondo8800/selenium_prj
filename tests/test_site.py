import time

import pytest

from pom.login import Login
from pom.main_page import MainPage


@pytest.mark.usefixtures('setup')
class TestSite:

    def test_fonts(self):
        """Check fonts"""
        right_title = MainPage(self.driver)
        expected_font = 'Arial, Helvetica, "Helvetica Neue", sans-serif'
        actual_font = right_title.get_right_title_text()
        assert expected_font == actual_font

    @pytest.mark.xfail(reason="expected_font set wrong")
    def test_fonts2(self):
        """Check fonts 2"""
        right_title = MainPage(self.driver)
        expected_font = 'rial, Helvetica, "Helvetica Neue", sans-serif'
        actual_font = right_title.get_right_title_text()
        assert expected_font == actual_font

    def test_fonts3(self):
        """Check fonts 3"""
        right_title = MainPage(self.driver)
        expected_font = 'Arial, Helvetica, "Helvetica Neue", sans-serif'
        actual_font = right_title.get_right_title_text()
        assert expected_font == actual_font
