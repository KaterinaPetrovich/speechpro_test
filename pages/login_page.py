from locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "http://localhost:5000/login"
    locators = LoginLocators()