import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable(Locators.LOGIN_BUTTON_ON_THE_MAIN_PAGE)).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys('sabinagracheva5111@ya.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys('112233')
    driver.find_element(*Locators.LOGIN_BUTTON_ON_THE_LOGIN_PAGE).click()
    return driver
