from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from locators import Locators


class TestLogout:
    # выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_personal_account(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, '//button[text()="Выход"]'))).click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, '//h2[text()="Вход"]'))).text
        assert text == "Вход"
