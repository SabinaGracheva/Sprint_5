from random import randint
from time import sleep
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

faker = Faker()


class TestRegistration:
    def test_registration_successful(self, driver):
        name = faker.name()
        email = faker.email()
        password = randint(100000, 999999)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REG_BUTTON_IN_ENTRY))
        driver.find_element(*Locators.REG_BUTTON_IN_ENTRY).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REG_INPUT))
        reg_input = driver.find_elements(*Locators.REG_INPUT)
        reg_input[0].send_keys(name)
        reg_input[1].send_keys(email)
        reg_input[2].send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        # Проверка успешной регистрации, авторизация под созданным юзером
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.EMAIL_ENTRY)).send_keys(email)
        driver.find_element(*Locators.PASSWORD_ENTRY).send_keys(password)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        sleep(3)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        sleep(3)
        assert driver.find_element(By.XPATH, "//button[text()='Выход']")

    def test_registration_invalid_password(self, driver):
        name = faker.name()
        email = faker.email()
        password = randint(10000, 99999)
        driver.find_element(*Locators.ENTRY_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REG_BUTTON_IN_ENTRY))
        driver.find_element(*Locators.REG_BUTTON_IN_ENTRY).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REG_INPUT))
        reg_input = driver.find_elements(*Locators.REG_INPUT)
        reg_input[0].send_keys(name)
        reg_input[1].send_keys(email)
        reg_input[2].send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert driver.find_element(By.XPATH, '//p[text()="Некорректный пароль"]')
