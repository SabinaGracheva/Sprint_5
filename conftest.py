import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,600")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.EMAIL_ENTRY).send_keys('sabinagracheva5111@ya.ru')
    driver.find_element(*Locators.PASSWORD_ENTRY).send_keys('112233')
    driver.find_element(*Locators.ENTRY_BUTTON).click()
    return driver
