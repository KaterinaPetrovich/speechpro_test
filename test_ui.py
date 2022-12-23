from base import BaseCase


class TestUI(BaseCase):

    def test_valid_register(self, random_email, random_name):
        self.driver.get(self.register_page.url)

        self.register_page.send_keys(self.register_page.locators.EMAIL_FIELD, random_email)
        self.register_page.send_keys(self.register_page.locators.PASSWORD_FIELD, "passwd3456")
        self.register_page.send_keys(self.register_page.locators.NAME_FIELD, random_name)
        self.register_page.click(self.register_page.locators.SIGN_UP_BUTTON)

        assert self.login_page.find(self.login_page.locators.TITLE)

    def test_without_name_register(self, random_email):
        self.driver.get(self.register_page.url)

        self.register_page.send_keys(self.register_page.locators.EMAIL_FIELD, random_email)
        self.register_page.send_keys(self.register_page.locators.PASSWORD_FIELD, "passwd3456")
        self.register_page.click(self.register_page.locators.SIGN_UP_BUTTON)

        assert self.login_page.find(self.login_page.locators.TITLE)