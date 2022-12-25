from locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "http://localhost:5000/login"
    locators = LoginLocators()

    def login(self, email, password):
        self.driver.get(self.url)
        self.send_keys(self.locators.EMAIL_FIELD, email)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_BUTTON)