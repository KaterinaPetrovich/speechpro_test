import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.register_page: RegisterPage = RegisterPage(driver)
        self.login_page: LoginPage = LoginPage(driver)
        self.profile_page: ProfilePage = ProfilePage(driver)
        self.home_page: HomePage = HomePage(driver)
