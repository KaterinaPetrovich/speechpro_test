from locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    url = "http://localhost:5000/profile"
    locators = ProfileLocators()
