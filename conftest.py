import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import UrlStellarBurgers
from data import PersonalInformationStellarBurgers
from locators import MainPageLocators
from locators import AuthPageLocators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(UrlStellarBurgers.URL)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonalInformationStellarBurgers.EMAIL)
    driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonalInformationStellarBurgers.PASSWORD)
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    return driver
