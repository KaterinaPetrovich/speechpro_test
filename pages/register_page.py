from locators import RegisterLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    url = "http://localhost:5000/signup"
    locators = RegisterLocators()