import pytest

from base import BaseCase


class TestUI(BaseCase):

    def test_valid_register(self, random_email, random_name, random_password):

        self.register_page.register(random_email, random_password, random_name)
        assert self.login_page.find(self.login_page.locators.TITLE)

    def test_without_name_register(self, random_email, random_password):

        self.register_page.register(random_email, random_password)
        assert self.login_page.find(self.login_page.locators.TITLE)

    @pytest.mark.parametrize("input_email", ["fjfjj89", " @ ", ",@mail.ru"])
    def test_invalid_email_register(self, input_email, random_password):
        self.register_page.register(input_email, random_password)
        assert self.driver.current_url == self.register_page.url

    def test_email_without_domain_name_register(self, random_name, random_password):
        self.register_page.register(f'{random_name}@{random_name}', random_password)
        assert self.driver.current_url == self.register_page.url

    def test_empty_email_register(self,  random_password):
        self.register_page.register("", random_password)

        assert self.driver.current_url == self.register_page.url
        assert not self.register_page.is_present(
            self.register_page.locators.ALREADY_EXIST_NOTIFICATION)

    def test_empty_password_register(self, random_email):
        self.register_page.register(random_email, "")

        assert self.driver.current_url == self.register_page.url

    def test_registered_email_register(self, random_email, random_password):
        self.register_page.register(random_email, random_password)
        self.register_page.register(random_email, random_password)

        assert self.driver.current_url == self.register_page.url
        assert self.register_page.is_present(
            self.register_page.locators.ALREADY_EXIST_NOTIFICATION)

    def test_short_password_register(self, random_email):
        self.register_page.register(random_email, "1")

        assert self.driver.current_url == self.register_page.url

    def test_space_password_register(self, random_email):

        self.register_page.register(random_email, " ")

        assert self.driver.current_url == self.register_page.url

    def test_login(self, random_email, random_password):
        self.register_page.register(random_email, random_password)
        self.login_page.login(random_email, random_password)

        assert self.driver.current_url == self.profile_page.url
        assert self.profile_page.find(self.profile_page.locators.TITLE)

    def test_lowercase_password_register_uppercase_login(self, random_email):
        self.register_page.register(random_email, "password")
        self.login_page.login(random_email, "PASSWORD")

        assert self.driver.current_url == self.login_page.url
        assert self.login_page.find(self.login_page.locators.WRONG_DETAILS_NOTIFICATION)

    def test_lowercase_email_register_uppercase_login(self, random_password):
        self.register_page.register("kate@mail.ru", random_password)
        self.login_page.login("KATE@mail.ru", random_password)
        assert self.driver.current_url == self.profile_page.url
        assert self.profile_page.find(self.profile_page.locators.TITLE)

    def test_wrong_password_login(self, random_email, random_password):
        self.register_page.register(random_email, random_password)
        self.login_page.login(random_email, "wrong_pass")

        assert self.driver.current_url == self.login_page.url
        assert self.login_page.find(self.login_page.locators.WRONG_DETAILS_NOTIFICATION)

    def test_empty_password_login(self, random_email):
        passwd = ""
        self.register_page.register(random_email, passwd)
        self.login_page.login(random_email, passwd)

        assert self.driver.current_url == self.login_page.url

    def test_logout(self, random_email, random_password):
        self.register_page.register(random_email, random_password)
        self.login_page.login(random_email, random_password)
        self.profile_page.click(self.profile_page.locators.LOGOUT)

        assert self.driver.current_url == self.home_page.url
        assert self.home_page.find(self.home_page.locators.LOGIN_HEADER)

