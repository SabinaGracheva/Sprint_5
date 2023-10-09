from random import randint
from faker import Faker
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from locators import AuthPageLocators
from locators import RegPageLocators
from locators import PersonalAccountPageLocators


faker = Faker()


class TestRegistration:
    def test_registration_successful(self, driver):
        name = faker.name()
        email = faker.email()
        password = randint(100000, 999999)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(AuthPageLocators.REG_BUTTON_IN_ENTRY)).click()
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RegPageLocators.REG_BUTTON))
        driver.find_element(*RegPageLocators.CREATE_NAME).send_keys(name)
        driver.find_element(*RegPageLocators.CREATE_EMAIL).send_keys(email)
        driver.find_element(*RegPageLocators.CREATE_PASSWORD).send_keys(password)
        driver.find_element(*RegPageLocators.REG_BUTTON).click()
        # Проверка успешной регистрации, авторизация под созданным юзером
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(AuthPageLocators.LOGIN_BUTTON))
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        logout = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        assert logout.is_displayed()

    def test_registration_invalid_password(self, driver):
        name = faker.name()
        email = faker.email()
        password = randint(10000, 99999)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(AuthPageLocators.REG_BUTTON_IN_ENTRY)).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(RegPageLocators.REG_BUTTON))
        driver.find_element(*RegPageLocators.CREATE_NAME).send_keys(name)
        driver.find_element(*RegPageLocators.CREATE_EMAIL).send_keys(email)
        driver.find_element(*RegPageLocators.CREATE_PASSWORD).send_keys(password)
        driver.find_element(*RegPageLocators.REG_BUTTON).click()
        assert driver.find_element(*RegPageLocators.ERR_MESSAGE)
