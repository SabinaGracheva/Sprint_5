from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from locators import Locators


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_button_login_account_main_page(self, driver, login):
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"

    # вход через кнопку «Личный кабинет»
    def test_login_button_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys('sabinagracheva5111@ya.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys('112233')
        driver.find_element(*Locators.LOGIN_BUTTON_ON_THE_LOGIN_PAGE).click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"

    # вход через кнопку в форме регистрации
    def test_login_button_in_registration_form(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.LOGIN_BUTTON_ON_THE_MAIN_PAGE)).click()
        driver.find_element(By.XPATH, '//a[text()="Зарегистрироваться"]').click()
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys('sabinagracheva5111@ya.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys('112233')
        driver.find_element(*Locators.LOGIN_BUTTON_ON_THE_LOGIN_PAGE).click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"

    # вход через кнопку в форме восстановления пароля
    def test_login_button_via_password_recovery(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.LOGIN_BUTTON_ON_THE_MAIN_PAGE)).click()
        driver.find_element(By.XPATH, '//a[text()="Восстановить пароль"]').click()
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys('sabinagracheva5111@ya.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys('112233')
        driver.find_element(*Locators.LOGIN_BUTTON_ON_THE_LOGIN_PAGE).click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"
