from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class TestLogin:
    # переход по клику на «Личный кабинет»
    def test_login_go_to_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys('sabinagracheva5111@ya.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys('112233')
        driver.find_element(*Locators.LOGIN_BUTTON_ON_THE_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
