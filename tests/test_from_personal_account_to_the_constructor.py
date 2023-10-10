from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators


class TestFromPersonalAccountToTheConstructor:
    # переход из ЛК по клику на «Конструктор»
    def test_from_personal_account_in_constructor(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        constructor = driver.find_elements(*MainPageLocators.CONSTRUCTOR)
        constructor[0].click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"

    # переход из ЛК по клику на логотип Stellar Burgers
    def test_from_personal_account_in_stellar_burgers(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        constructor = driver.find_elements(*MainPageLocators.CONSTRUCTOR)
        constructor[1].click()
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"
