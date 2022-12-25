from locators import RegisterLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    url = "http://localhost:5000/signup"
    locators = RegisterLocators()

    def register(self, email, password, name=''):
        self.driver.get(self.url)

        self.send_keys(self.locators.EMAIL_FIELD, email)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.send_keys(self.locators.NAME_FIELD, name)
        self.click(self.locators.SIGN_UP_BUTTON)
