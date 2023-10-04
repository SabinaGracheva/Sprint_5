from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By

class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_button_login_account(self, driver, login):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN_PAGE)).click()
        sleep(5)
        
