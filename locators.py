from selenium.webdriver.common.by import By

SIGN_UP_HEADER = (By.XPATH, '//a[@href = "/signup"]')
LOGIN_HEADER = (By.XPATH, '//a[@href = "/login"]')


class RegisterLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@name = "email"]')
    NAME_FIELD = (By.XPATH, '//input[@name = "name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name = "password"]')
    SIGN_UP_BUTTON = (By.XPATH, '//button[text()[contains(.,"Sign Up")]]')


class LoginLocators:
    TITLE = (By.XPATH, '//h3[text()[contains(.,"Login")]]')
    NAME_FIELD = (By.XPATH, '//input[@name = "name"]')
