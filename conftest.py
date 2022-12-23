import random
import string

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def random_email():
    random_str = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return f'{random_str}@mail.ru'


@pytest.fixture()
def random_name():
    random_str = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    return random_str


@pytest.fixture()
def random_password():
    random_str = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    return random_str