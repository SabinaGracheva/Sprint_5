from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import PersonalInformationStellarBurgers
from locators import MainPageLocators, PersonalAccountPageLocators, AuthPageLocators, RegPageLocators, \
    RestorePasswordPageLocators


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_button_login_account_main_page(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        logout = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        assert logout.is_displayed()

    # вход через кнопку «Личный кабинет»
    def test_login_button_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonalInformationStellarBurgers.EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonalInformationStellarBurgers.PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        logout = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        assert logout.is_displayed()

    # вход через кнопку в форме регистрации
    def test_login_button_in_registration_form(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        driver.find_element(*AuthPageLocators.REG_BUTTON_IN_ENTRY).click()
        driver.find_element(*RegPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonalInformationStellarBurgers.EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonalInformationStellarBurgers.PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        logout = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        assert logout.is_displayed()

    # вход через кнопку в форме восстановления пароля
    def test_login_button_via_password_recovery(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        driver.find_element(*AuthPageLocators.RESTORE_PASSWORD).click()
        driver.find_element(*RestorePasswordPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonalInformationStellarBurgers.EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonalInformationStellarBurgers.PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        logout = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        assert logout.is_displayed()
