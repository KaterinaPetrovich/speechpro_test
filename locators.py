from selenium.webdriver.common.by import By

SIGN_UP_HEADER = (By.XPATH, '//a[@href = "/signup"]')
LOGIN_HEADER = (By.XPATH, '//a[@href = "/login"]')


class RegisterLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@name = "email"]')
    NAME_FIELD = (By.XPATH, '//input[@name = "name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name = "password"]')
    SIGN_UP_BUTTON = (By.XPATH, '//button[text()[contains(.,"Sign Up")]]')
    ALREADY_EXIST_NOTIFICATION = \
        (By.XPATH, '//div[text()[contains(.,"Email address already exists")]]')


class LoginLocators:
    TITLE = (By.XPATH, '//h3[text()[contains(.,"Login")]]')
    EMAIL_FIELD = (By.XPATH, '//input[@name = "email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name = "password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()[contains(.,"Login")]]')
    WRONG_DETAILS_NOTIFICATION = \
        (By.XPATH, '//div[text()[contains(.,"Please check your login details")]]')


class ProfileLocators:
    TITLE = (By.XPATH, '//h1[text()[contains(.,"Welcome")]]')
