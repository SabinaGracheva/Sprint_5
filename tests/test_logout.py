from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, PersonalAccountPageLocators, AuthPageLocators


class TestLogout:
    # выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_personal_account(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON)).click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(AuthPageLocators.LOGIN_TEXT)).text
        assert text == "Вход"
