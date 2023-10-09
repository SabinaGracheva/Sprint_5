from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import PersonalInformationStellarBurgers
from locators import MainPageLocators, AuthPageLocators, PersonalAccountPageLocators


class TestLogin:
    # переход по клику на «Личный кабинет»
    def test_login_go_to_personal_account(self, driver):
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
