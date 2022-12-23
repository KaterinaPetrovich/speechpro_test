
import pytest

from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.register_page:RegisterPage = RegisterPage(driver)
        self.login_page:LoginPage = LoginPage(driver)